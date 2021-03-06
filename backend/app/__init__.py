"""
__init__.py
 creates a Flask app instance and registers the database object
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

# Bibliotecas publicamente acessíveis
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig') # Development Server
 
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Inicializa Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Inclui os models
        from . import models

        from .api import api
        app.register_blueprint(api, url_prefix="/api")
        return app  

