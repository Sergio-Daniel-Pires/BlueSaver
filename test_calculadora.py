import pytest
from .app import app as app_

def test_calculator_valid_key():
    """
    Testa se a resposta do `POST` da rota "/calculadora/calcular"
    com dados válidos contém as chaves esperadas no objeto JSON retornado.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'sudeste'})

    data = response.get_json()
    assert 'gasto_agua' in data
    assert 'gasto_pessoa' in data


def test_calculator_valid_status():
    """
    Testa se a resposta do `POST` da rota "/calculadora/calcular"
    com dados válidos tem status 200 OK.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'sudeste'})

    assert response.status_code == 200

def test_calculator_invalid_key_error():
    with app_.test_client() as client:
        with pytest.raises(KeyError):
            response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'São Paulo'})


def test_calculator_valid_content_type():
    """
    Testa se a resposta do `POST` da rota "/calculadora/calcular"
    com dados válidos possui o tipo de conteúdo JSON.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'sudeste'})

    assert response.headers['Content-Type'] == 'application/json'