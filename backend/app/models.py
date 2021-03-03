"""
models.py
- Defines this project's models for SQL-Alchemy
"""

from . import db 

class Acao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), index=True, unique=True)
    dy = db.Column(db.Integer)
    patr_liq = db.Column(db.BigInteger)
    roe = db.Column(db.Integer)
    vpa = db.Column(db.Integer)
    lpa = db.Column(db.Integer)
    n_acoes = db.Column(db.BigInteger)
    lucro_liq = db.Column(db.BigInteger)
    payout = db.Column(db.Integer)
    margem_liq = db.Column(db.Integer)
    cres5 = db.Column(db.Integer)

    def __repr__(self):
        return '<ACAO {}>'.format(self.ticker)

    @staticmethod
    def to_storage_format(float_num):
        return int(float_num*10000)

    @staticmethod
    def to_real_format(int_num):
        return int_num/10000.0
