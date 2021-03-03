
import pandas as pd
import re
import urllib.request
import urllib.parse
import http.cookiejar

from lxml.html import fragment_fromstring
from collections import OrderedDict
from . import db  
from .models import Acao
        

# Get data from www.fundamentos.com.br
# Credits: Phoemur (https://github.com/phoemur/fundamentus/blob/master/fundamentus.py)
def get_data(*args, **kwargs):
    url = 'http://www.fundamentus.com.br/resultado.php'
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                         ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]

    # Aqui estão os parâmetros de busca das ações
    # Estão em branco para que retorne todas as disponíveis
    data = {'pl_min': '',
            'pl_max': '',
            'pvp_min': '',
            'pvp_max' : '',
            'psr_min': '',
            'psr_max': '',
            'divy_min': '',
            'divy_max': '',
            'pativos_min': '',
            'pativos_max': '',
            'pcapgiro_min': '',
            'pcapgiro_max': '',
            'pebit_min': '',
            'pebit_max': '',
            'fgrah_min': '',
            'fgrah_max': '',
            'firma_ebit_min': '',
            'firma_ebit_max': '',
            'margemebit_min': '',
            'margemebit_max': '',
            'margemliq_min': '',
            'margemliq_max': '',
            'liqcorr_min': '',
            'liqcorr_max': '',
            'roic_min': '',
            'roic_max': '',
            'roe_min': '',
            'roe_max': '',
            'liq_min': '',
            'liq_max': '',
            'patrim_min': '',
            'patrim_max': '',
            'divbruta_min': '',
            'divbruta_max': '',
            'tx_cresc_rec_min': '',
            'tx_cresc_rec_max': '',
            'setor': '',
            'negociada': 'ON',
            'ordem': '1',
            'x': '28',
            'y': '16'}

    with opener.open(url, urllib.parse.urlencode(data).encode('UTF-8')) as link:
        content = link.read().decode('ISO-8859-1')

    pattern = re.compile('<table id="resultado".*</table>', re.DOTALL)
    content = re.findall(pattern, content)[0]
    page = fragment_fromstring(content)
    result = OrderedDict()

    for rows in page.xpath('tbody')[0].findall("tr"):
        result.update({rows.getchildren()[0][0].getchildren()[0].text: {'Cotacao': to_float(rows.getchildren()[1].text),
                                                                        'P/L': to_float(rows.getchildren()[2].text),
                                                                        'P/VP': to_float(rows.getchildren()[3].text),
                                                                        'PSR': to_float(rows.getchildren()[4].text),
                                                                        'DY': to_float(rows.getchildren()[5].text),
                                                                        'P/Ativo': to_float(rows.getchildren()[6].text),
                                                                        'P/Cap.Giro': to_float(rows.getchildren()[7].text),
                                                                        'P/EBIT': to_float(rows.getchildren()[8].text),
                                                                        'P/ACL': to_float(rows.getchildren()[9].text),
                                                                        'EV/EBIT': to_float(rows.getchildren()[10].text),
                                                                        'EV/EBITDA': to_float(rows.getchildren()[11].text),
                                                                        'Mrg.Ebit': to_float(rows.getchildren()[12].text),
                                                                        'Mrg.Liq.': to_float(rows.getchildren()[13].text),
                                                                        'Liq.Corr.': to_float(rows.getchildren()[14].text),
                                                                        'ROIC': to_float(rows.getchildren()[15].text),
                                                                        'ROE': to_float(rows.getchildren()[16].text),
                                                                        'Liq.2meses': to_float(rows.getchildren()[17].text),
                                                                        'Pat.Liq': to_float(rows.getchildren()[18].text),
                                                                        'Div.Brut/Pat.': to_float(rows.getchildren()[19].text),
                                                                        'Cresc.5anos': to_float(rows.getchildren()[20].text)}})
    
    dataframe_result = pd.DataFrame(result, columns=result.keys()).transpose()
    dataframe_filtered = dataframe_result.copy()
    for ticker in dataframe_result.index:
        if (dataframe_result.loc[ticker]['P/L'] <= 0 or dataframe_result.loc[ticker]['P/VP'] <= 0):
            dataframe_filtered.drop(index=ticker, inplace=True)
            
        
    return dataframe_filtered
    
def to_float(string):
  string = string.replace('.', '')
  string = string.replace(',', '.')

  if (string.endswith('%')):
    string = string[:-1]
    return float(string) / 100
  else:
    return float(string)


def fetch_ativo(ticker, data_fundamentos):
    LPA = data_fundamentos.loc[ticker]['Cotacao']/data_fundamentos.loc[ticker]['P/L']
    VPA = data_fundamentos.loc[ticker]['Cotacao']/data_fundamentos.loc[ticker]['P/VP']
    N_acoes = int(data_fundamentos.loc[ticker]['Pat.Liq']/VPA)
    Lucro_Liquido = int(N_acoes * LPA)
    Payout = data_fundamentos.loc[ticker]['DY']*data_fundamentos.loc[ticker]['P/L']

    data_useful = {
        'DY': data_fundamentos.loc[ticker]['DY'],
        'PatrimonioLiq': data_fundamentos.loc[ticker]['Pat.Liq'],
        'ROE': data_fundamentos.loc[ticker]['ROE'],
        'VPA': VPA,
        'LPA': LPA,
        'N_acoes': N_acoes,
        'LucroLiq': Lucro_Liquido,
        'Payout': Payout,
        'MargemLiq': data_fundamentos.loc[ticker]['Mrg.Liq.'],
        'Cres5': data_fundamentos.loc[ticker]['Cresc.5anos']
    }
    
    return data_useful
    

def update_sql():
    acoes_df = get_data()
    for ticker in acoes_df.index:
        dados = fetch_ativo(ticker, acoes_df)
        acao_existente = Acao.query.filter_by(ticker=ticker).first()
        if acao_existente is not None:
            acao_existente.dy = Acao.to_storage_format(dados['DY'])
            acao_existente.patr_liq = dados['PatrimonioLiq']
            acao_existente.roe = Acao.to_storage_format(dados['ROE'])
            acao_existente.vpa = Acao.to_storage_format(dados['VPA'])
            acao_existente.lpa = Acao.to_storage_format(dados['LPA'])
            acao_existente.n_acoes = dados['N_acoes']
            acao_existente.lucro_liq = dados['LucroLiq']
            acao_existente.payout = Acao.to_storage_format(dados['Payout'])
            acao_existente.margem_liq = Acao.to_storage_format(dados['MargemLiq'])
            acao_existente.cres5 = Acao.to_storage_format(dados['Cres5'])
        else:
            acao = Acao(
                ticker=ticker, 
                dy=Acao.to_storage_format(dados['DY']),
                patr_liq=dados['PatrimonioLiq'],
                roe=Acao.to_storage_format(dados['ROE']),
                vpa=Acao.to_storage_format(dados['VPA']),
                lpa=Acao.to_storage_format(dados['LPA']),
                n_acoes=dados['N_acoes'],
                lucro_liq=dados['LucroLiq'],
                payout=Acao.to_storage_format(dados['Payout']),
                margem_liq=Acao.to_storage_format(dados['MargemLiq']),
                cres5=Acao.to_storage_format(dados['Cres5'])
            )
            db.session.add(acao)
    
    db.session.commit()


    


