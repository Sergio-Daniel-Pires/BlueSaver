import os
from pathlib import Path

class BaseConfig():
    """Configuracao basica BlueSaver API"""
    BASE_DIR = Path(__file__)
    STATIC = os.path.join(BASE_DIR, 'STATICS')



class DevelopConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    DEBUG = True

config = {
    "development": DevelopConfig,
    "production": ProdConfig
}
