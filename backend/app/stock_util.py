# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:55:05 2021

@author: berna
"""
from . import db  
from .models import Acao
from yahooquery import Ticker
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

def get_acao(ticker):
    acao = Acao.query.filter_by(ticker=ticker).first()
    return acao

# OK
def get_receitaliquida(lucro_liq, margem_liq):
    if margem_liq != 0:
        return lucro_liq/margem_liq
    else: 
        return 0

# Ver como fazer
def get_resultadonaoop(ticker):
    return 0

# Pegar cotacao do momento usando yahooquery (dinamico com preco)
def get_cotacao(ticker):
    if (get_acao(ticker) is not None):
        acao = Ticker(ticker+'.SA')
        preco = acao.price[ticker+'.SA']['regularMarketPrice']
        return preco
    else: 
        return 0

# Dinamico com preco
def get_precolucro(ticker, lpa):
    return get_cotacao(ticker)/lpa

# Pegar historico de preços da ação usando yahooquery
def get_historico(ticker):
    if (get_acao(ticker) is not None):
        acao = Ticker(ticker+'.SA')
        historico = acao.history(period="10y", interval="1d")
        historico_index_reset = historico.reset_index()
        return historico_index_reset
    else: 
        return None

def get_historico_plot_json(ticker, precojusto):
    historico = get_historico(ticker)
    if (historico is not None):
        data=[go.Candlestick(x=historico['date'], open=historico['open'], high=historico['high'], low=historico['low'], close=historico['close'])]
        fig = go.Figure(data)

        # Change the Candle Mode
        fig.update_layout(
            autosize=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        fig.add_hline(y=precojusto, line_width=2, 
                      line_color="LightGreen", 
                      line_dash="dash", 
                      annotation_text="Preço Calculado: R$ " + str(precojusto), 
                      annotation_position="bottom")

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON
    else:
        return 0