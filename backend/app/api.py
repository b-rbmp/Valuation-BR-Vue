"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""
from flask import Blueprint, jsonify, request
from .stock_api_wrapper import update_sql
from .calculos import calculo_graham, calculo_lynch_ROE, calculo_lynch_CRES, calculo_psbe, calculo_upside
from .stock_util import get_cotacao, get_acao, get_historico, get_used_calculated_data
from .models import Acao

api = Blueprint('api', __name__)

@api.route('/ativo/<string:ativo>/', methods=('GET', 'POST'))
def ativo(ativo):
    if request.method == 'GET':
      ativoFound = get_acao(ativo)
      if ativoFound is not None and Acao.to_real_format(ativoFound.lpa) > 0 and Acao.to_real_format(ativoFound.vpa) > 0 :
        response_object = { 'status': "success" }
        preco_psbe = calculo_psbe(ativo)
        preco_graham = calculo_graham(ativo)
        preco_lynch_roe = calculo_lynch_ROE(ativo)
        preco_lynch_cres = calculo_lynch_CRES(ativo)
        cotacao = get_cotacao(ativo)

        response_object['preco_psbe'] = preco_psbe
        response_object['preco_graham'] = preco_graham
        response_object['preco_lynch_roe'] = preco_lynch_roe
        response_object['preco_lynch_cres'] = preco_lynch_cres
        response_object['cotacao'] = cotacao
        response_object['upside_psbe'] = calculo_upside(cotacao, preco_psbe)
        response_object['upside_graham'] = calculo_upside(cotacao, preco_graham)
        response_object['upside_lynch_roe'] = calculo_upside(cotacao, preco_lynch_roe)
        response_object['upside_lynch_cres'] = calculo_upside(cotacao, preco_lynch_cres)
        response_object['stockdata'] = get_used_calculated_data(ativo)
        historico_preco = get_historico(ativo)
        response_object['historico'] = historico_preco.to_dict()
        return jsonify(response_object)
      else:
        response_object = { 'status': '404' }
        return jsonify(response_object)

    elif request.method == 'POST':
      response_object = { 'status': "success" }
      return jsonify(response_object)


@api.route('/ativos/')
def ativos():
  ativos = Acao.query.all()
  return jsonify({ 'ativos': [acao.ticker for acao in ativos] })

# @api.route('/search/<string:ativo>/')
# def search(ativo):

# Temporary
@api.route('/update/')
def update():
  update_sql()
  response_object = {'status': 'success'}
  return jsonify(response_object)
