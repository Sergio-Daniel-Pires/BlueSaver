from flask import Flask
from .config import config
import os

def create_app(config_name: str = None):
    app = Flask(__name__)
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "production")

    # Rotas das Features
    # Home
    from views.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/')
    
    # Graficos
    from views.graficos import graficos_bp
    app.register_blueprint(graficos_bp, url_prefix='/graficos')

    # Quiz
    from views.quiz import quiz_bp
    app.register_blueprint(quiz_bp, url_prefix='/quiz')

    # Calculadora de consumo de água
    from views.calculadora import calculadora_bp
    app.register_blueprint(calculadora_bp, url_prefix='/calculadora')

    # Dicas para economizar agua
    from views.dicas import dicas_bp
    app.register_blueprint(dicas_bp, url_prefix='/dicas')

    # Configuracao Flask
    app.config.from_object(config[config_name])

    return app

app = create_app("development")