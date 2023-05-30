from flask import Flask
from flask_restx import Api
from .config import config
import os

api = Api(
    title="BlueSaver - MC426",
    version="1.0",
    doc="/docs",
    description="Projeto com várias funcionalidades sobre a aplicação/uso da água na nossa sociedade",
)

def create_app(config_name: str = None):
    app = Flask(__name__)
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "production")

    # Rotas das Features
    # Home
    from .features.home.views import home_ns
    api.add_namespace(home_ns, path='/home')
    
    # Graficos
    from .features.graficos.views import graficos_ns
    api.add_namespace(graficos_ns, path='/graficos')

    # Quiz
    from .features.quiz.views import quiz_ns
    api.add_namespace(quiz_ns, path='/quiz')

    # Configuracao Flask
    app.config.from_object(config[config_name])
    api.init_app(app)

    return app

app = create_app("development")