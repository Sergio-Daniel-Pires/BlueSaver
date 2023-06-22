import pytest
from .app import app as app_

def test_get_content_type():
    """
        Testa se o `content_type` da resposta do `GET` da rota quiz
        é um template HTML renderizado corretamente.
    """
    with app_.test_client() as client:
        response = client.get('/quiz/')

    assert response.content_type == 'text/html; charset=utf-8'

def test_post_content_type():
    """
        Testa se o `content_type` da resposta do `POST` da rota quiz
        é um json.
    """
    with app_.test_client() as client:
        response = client.post('/quiz/')

    assert response.content_type == 'application/json'

def test_post_dificulty_easy():
    """
        Testa se o quiz de dificuldade `Fácil` existe.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert "Fácil" in json_data

def test_post_dificulty_intermediary():
    """
        Testa se o quiz de dificuldade `Médio` existe.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert "Médio" in json_data

def test_post_dificulty_hard():
    """
        Testa se o quiz de dificuldade `Difícil` existe.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert "Difícil" in json_data

@pytest.mark.parametrize("dificuldade", [
    "Difíci",
    "difícil",
    "Muito Difícil",
    "Fáci",
    "Fácill",
    "1",
    ""
])
def test_post_dificulty_border_case(dificuldade):
    """
        Testa se o quiz, de dificuldades semelhantes
        às existentes, não existem.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert dificuldade not in json_data