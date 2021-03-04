"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""
from flask import Blueprint, jsonify, request
from .stock_api_wrapper import update_sql
from .calculos import calculo_dcf, calculo_graham, calculo_lynch_ROE, calculo_lynch_CRES, calculo_psbe, calculo_upside
from .stock_util import get_cotacao, get_acao, get_historico
from .models import Acao

api = Blueprint('api', __name__)

@api.route('/ativo/<string:ativo>/')
def ativo(ativo):
    response = { 'msg': "Hello {}".format(ativo)}
    return jsonify(response)

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
