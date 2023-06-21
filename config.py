import os
from pathlib import Path

class BaseConfig():
    """Configuracao basica BlueSaver API"""
    BASE_DIR = Path(__file__).parent
    STATIC = os.path.join(BASE_DIR, 'static')

class DevelopConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    DEBUG = False

config = {
    "development": DevelopConfig,
    "production": ProdConfig
}
