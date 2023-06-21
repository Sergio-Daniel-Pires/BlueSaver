import pytest
from .app import app as app_
from .features.quiz.quiz_funcoes import escolher_perguntas, verifica_resposta

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

def test_verify_answer_all_correct(static):
    output = verifica_resposta('Fácil', ['a', 'c', 'b', 'c'], static)
    assert "Incorreta" not in str(output)

def test_verify_answer_incorrect(static):
    output = verifica_resposta('Fácil', ['a', 'a', 'a', 'a'], static)
    assert "Incorreta" in str(output)

def test_graph_8_years():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Até 8 anos!"})

    assert response.status_code == 200

def test_graph_9_to_15():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Entre 9 e 15!"})

    assert response.status_code == 200

def test_graph_up_to_16():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "16 ou mais!"})

    assert response.status_code == 200

def test_graph_mimetype_image():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "16 ou mais!"})

    assert response.headers['content-type'] == "image/png"

def test_graph_no_parameter_idade():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar")

    assert response.status_code == 400

def test_invalid_parameter_idade():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Corta pra 18"})

    assert response.status_code == 400
