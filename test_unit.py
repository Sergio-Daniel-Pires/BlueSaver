import pytest
from .app import app as app_
from .views.quiz import escolher_perguntas, verifica_resposta

@pytest.fixture
def static():
    return 'static'

def test_generate_quiz_post():
    with app_.test_client() as client:
        response = client.post('/quiz/')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        json_data = response.get_json()
        assert isinstance(json_data, dict)
        assert 'Fácil' in json_data
        
def test_post_dificulty_facil(static):
    """
        Testa se o quiz de dificuldade `Fácil` existe.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert "Fácil" in json_data

def test_post_dificulty_intermediary(static):
    """
        Testa se o quiz de dificuldade `Médio` existe.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert "Médio" in json_data

def test_post_dificulty_hard(static):
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
def test_post_dificulty_border_case(static, dificuldade):
    """
        Testa se o quiz, de dificuldades semelhantes
        às existentes, não existem.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
        json_data = response.get_json()
    
    assert dificuldade not in json_data

def test_graph_mimetype_image():
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")

    assert response.headers['content-type'] == "text/html; charset=utf-8"

def test_invalid_parameter_idade():
    with app_.test_client() as client:
        response = client.get("/graficos/18_old")

    assert response.status_code == 400
