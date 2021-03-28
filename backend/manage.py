# -*- coding: utf-8 -*-
"""
manage.py
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup
"""

from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import Acao
from app.stock_api_wrapper import update_sql

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# Commands
class UpdateSql(Command):
    "updates the sql"

    def run(self):
        update_sql()

# provide a migration utility command
manager.add_command('db', MigrateCommand)
manager.add_command('updatesql', UpdateSql())

# enable python shell with application context
@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Acao=Acao)

if __name__ == '__main__':
    manager.run()