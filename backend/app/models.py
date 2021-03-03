"""
models.py
- Defines this project's models for SQL-Alchemy
"""

from . import db 
from datetime import datetime
class Acao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
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
        
    def to_dict(self):
        return dict(id=self.id,
                    ticker=self.ticker,
                    last_updated=self.last_updated.strftime('%Y-%m-%d %H:%M:%S'),
                    dy=self.dy,
                    patr_liq=self.patr_liq,
                    roe=self.roe,
                    vpa=self.vpa,
                    lpa=self.lpa,
                    n_acoes=self.n_acoes,
                    lucro_liq=self.lucro_liq,
                    payout=self.payout,
                    margem_liq=self.margem_liq,
                    cres5=self.cres5)

    @staticmethod
    def to_storage_format(float_num):
        return int(float_num*10000)

    @staticmethod
    def to_real_format(int_num):
        return int_num/10000.0

