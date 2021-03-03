from . import stock_util as su
import math 
import numpy as np
from .models import Acao

def calculo_dcf(lpa, anos_prev, g_prev, g_term, taxa_desconto):
    taxa_desconto = float(taxa_desconto)*1.0/100
    g_term = float(g_term)*1.0/100
    g_prev = float(g_prev)*1.0/100
    lpa = float(lpa)
    valor_justo = 0.0
    for i in range(0, anos_prev):
        valor_justo = valor_justo + lpa*((1+g_prev)**(i+1))/((1+taxa_desconto)**(i+1))
    valor_justo = valor_justo + lpa*((1+g_prev)**(anos_prev))/((1+taxa_desconto)**(anos_prev))*(1+g_term)/(taxa_desconto-g_term)
    return round(valor_justo, 2)

# Dando erro pros bancos pois ta sem margem liquida
def calculo_psbe(ticker):
    acao = su.get_acao(ticker)
    if acao is not None:
        patr_liq = acao.patr_liq
        lucro_liq = acao.lucro_liq
        n_acoes = acao.n_acoes
        margem_liq = Acao.to_real_format(acao.margem_liq)
        rec_liq = su.get_receitaliquida(lucro_liq=lucro_liq, margem_liq=margem_liq)
        rec_naoop = 0 # @TODO
        constant_VMCM = 5.5 # Constante VMCM que indica a captação de fluxo financeiro na bolsa. 
        # @TODO CRIAR METODO P CALCULAR A CONSTANTE VMCM FAZENDO UM BEST FIT DESSA CONSTANTE, QUE É BASICAMENTE COMPARAR O PREÇO JUSTO COM A COTAÇÃO E FAZER O BEST FIT, LEMBRANDO
        # DE APENAS FAZER PARA EMPRESAS COM LUCRO LIQUIDO POSITIVO
        
        preco_justo = (patr_liq+rec_liq+rec_naoop+((lucro_liq-rec_naoop)*math.exp(margem_liq*(-math.log(margem_liq))*constant_VMCM*np.sign(margem_liq))))/n_acoes
        return round(preco_justo, 2)
    else:
        return 0

def calculo_graham(ticker):
    acao = su.get_acao(ticker)
    if acao is not None:
        lpa = Acao.to_real_format(acao.lpa)
        vpa = Acao.to_real_format(acao.vpa)
        preco_justo = math.sqrt(22.5*lpa*vpa)
        return round(preco_justo, 2)
    else:
        return 0

# Calculo com ROE
def calculo_lynch_ROE(ticker):
    acao = su.get_acao(ticker)
    if acao is not None:
        dividend_yield = Acao.to_real_format(acao.dy)
        crescimento = (1-Acao.to_real_format(acao.payout))*Acao.to_real_format(acao.roe) # Calculo de crescimento usando (1-Payout)*ROE.
        pegy = su.get_precolucro(ticker, Acao.to_real_format(acao.lpa))/((crescimento + dividend_yield)*100)
        preco_justo = su.get_cotacao(ticker)/pegy
        return round(preco_justo, 2)
    else:
        return 0

def calculo_lynch_CRES(ticker):
    acao = su.get_acao(ticker)
    if acao is not None:
        dividend_yield = Acao.to_real_format(acao.dy)
        crescimento = Acao.to_real_format(acao.cres5) # Calculo de crescimento usando Crescimento 5a (ver se uso CAGR 5A)
        pegy = su.get_precolucro(ticker, Acao.to_real_format(acao.lpa))/((crescimento + dividend_yield)*100)
        preco_justo = su.get_cotacao(ticker)/pegy
        return round(preco_justo, 2)
    else:
        return 0

def calculo_upside(cotacao_atual, preco_justo):
    if cotacao_atual != 0 and preco_justo != 0:
        return round((float(preco_justo)/float(cotacao_atual)-1)*100, 2)
    else: 
        return 0
