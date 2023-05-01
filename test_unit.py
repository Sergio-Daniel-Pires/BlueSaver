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