from flask import Flask, render_template
from .config import config
import os

def create_app(config_name: str = None):
    app = Flask(__name__)
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "production")

    # Rotas das Features
    # Graficos
    """
    from .features.graficos.views import graficos_ns
    api.add_namespace(graficos_ns, path='/graficos')

    # Quiz
    from .features.quiz.views import quiz_ns
    api.add_namespace(quiz_ns, path='/quiz')
    """
    from features.home.views import home_bp
    app.register_blueprint(home_bp)

    from features.graficos.views import grafico_bp
    app.register_blueprint(grafico_bp)

    from features.quiz.views import quiz_bp
    app.register_blueprint(quiz_bp)

    # Configuracao Flask
    app.config.from_object(config[config_name])

    return app

app = create_app("development")