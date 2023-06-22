import pytest
from .app import app as app_

def test_get_content_type():
    """
        Testa se o `content_type` da resposta do `GET` da rota chatGPT
        é um template HTML renderizado corretamente.
    """
    with app_.test_client() as client:
        response = client.get('/chatgpt/')

    assert response.content_type == 'text/html; charset=utf-8'