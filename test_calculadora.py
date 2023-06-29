import pytest
from .app import app as app_

def test_calculator_valid_status():
    """
    Testa se a resposta do `POST` da rota "/calculadora/calcular"
    com dados válidos contém as chaves esperadas no objeto JSON retornado.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'sudeste'})

    data = response.get_json()
    assert 'gasto_agua' in data
    assert 'gasto_pessoa' in data


def test_calculator_invalid_key_error():
    with app_.test_client() as client:
        with pytest.raises(KeyError):
            response = client.post('/calculadora/calcular', data={'qtd_pessoas': '4', 'gasto_mensal': '100', 'estado': 'São Paulo'})
