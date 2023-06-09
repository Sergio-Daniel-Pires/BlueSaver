import pytest
from .app import app as app_
from .views.quiz import escolher_perguntas, verifica_resposta

@pytest.fixture
def static():
    return 'static'

def test_gerar_dificulty_facil(static):
    output = escolher_perguntas("Fácil", static)
    assert output[1] == 200

def test_gerar_dificulty_intermediary(static):
    output = escolher_perguntas("Médio", static)
    assert output[1] == 200

def test_gerar_dificulty_hard(static):
    output = escolher_perguntas("Difícil", static)
    assert output[1] == 200

def test_gerar_invalid_dificulty(static):
    output = escolher_perguntas("Super Hard", static)
    assert output[1] == 400

def test_empty_quiz_difficulty():
    with app_.test_client() as client:
        response = client.post("/quiz/")
    
    assert response.status_code == 400

def test_verify_answer_all_correct(static):
    respostas = {
        "1": "a",
        "2": "c",
        "3": "b",
        "4": "c"
    }
    output = verifica_resposta('Fácil', respostas, static)
    
    assert output['resultado']['acertos'] == 4

def test_verify_answer_incorrect(static):
    respostas = {
        '1': 'a',
        '2': 'a',
        '3': 'a',
        '4': 'a'
    }
    output = verifica_resposta('Fácil', respostas, static)
    
    assert output['resultado']['acertos'] != 4

def test_graph_mimetype_image():
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")

    assert response.headers['content-type'] == "text/html; charset=utf-8"

def test_invalid_parameter_idade():
    with app_.test_client() as client:
        response = client.get("/graficos/18_old")

    assert response.status_code == 400
