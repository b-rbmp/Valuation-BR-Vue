# -*- coding: utf-8 -*-
"""
wsgi.py
- Starts the application
"""
from app import create_app, db
from app.models import Acao

app = create_app()
if __name__ == '__main__':
    app.run(host='127.0.0.1')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Acao': Acao}
