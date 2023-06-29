import pytest
from .app import app as app_

def test_calculator_valid_key():
    """
        Testa se a resposta do `POST` da rota "/calculadora/calcular"
        com dados válidos contém as chaves esperadas no objeto JSON retornado.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '4',
            'gasto_mensal': '100',
            'estado': 'sudeste'
        })

    data = response.get_json()
    assert 'gasto_agua' in data
    assert 'gasto_pessoa' in data


def test_calculator_valid_status():
    """
        Testa se a resposta do `POST` da rota "/calculadora/calcular"
        com dados válidos tem status 200 OK.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '4',
            'gasto_mensal': '100',
            'estado': 'sudeste'
        })

    assert response.status_code == 200

def test_calculator_invalid_key_error():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna 
        um `KeyError` se uma das chaves estiver errada.
    """
    with app_.test_client() as client:
        with pytest.raises(KeyError):
            response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '4',
            'gasto_mensal':'100',
            'estado': 'São Paulo'
        })

def test_calculator_valid_content_type():
    """
        Testa se a resposta do `POST` da rota "/calculadora/calcular"
        com dados válidos possui o tipo de conteúdo JSON.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '4',
            'gasto_mensal': '100',
            'estado': 'sudeste'
        })

    assert response.headers['Content-Type'] == 'application/json'

def test_calculator_invalid_input_type():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna 
        um `ValueError` se o tipo de uma das entradas estiver errado.
    """
    with app_.test_client() as client:
        with pytest.raises(ValueError):
            response = client.post('/calculadora/calcular', data={
                'qtd_pessoas': 'abc',
                'gasto_mensal': '100',
                'estado': 'sudeste'
            })

def test_calculator_invalid_input_none():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna status 400 Bad Request
        quando os dados de entrada são inválidos e se a mensagem de erro correta é retornada
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '4',
            'gasto_mensal': '100',
            'estado': None
        })
    
    assert response.status_code == 400
    assert response.data == b'Preencha os dados corretamente!'

def test_calculator_invalid_input_empty():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna status 400 Bad Request
        quando os dados de entrada são inválidos e se a mensagem de erro correta é retornada
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
        'qtd_pessoas': '',
        'gasto_mensal': '100',
        'estado': 'sudeste'
    })
    
    assert response.status_code == 400
    assert response.data == b'Os dados precisam ser inteiros validos!'

def test_calculator_valid_lower_limit_input():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna o cálculo realizado
        corretamente para valores mínimos, resposta com status 200 e JSON contendo as
        chaves 'gasto_agua', 'gasto_pessoa' com valores iguais a 0.
    """
    expected = {
        'gasto_agua': 0.0,
        'gasto_pessoa': 0.0
    }

    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '1',
            'gasto_mensal': '0',
            'estado': 'sudeste'
        })
    
    assert response.status_code == 200
    assert response.json == expected

def test_calculator_invalid_lower_limit_input():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna resposta
        com status 400 e o `None` no lugar dos dados.
    """
    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '-1',
            'gasto_mensal': '0',
            'estado': 'sudeste'
        })
    
    assert response.status_code == 400
    assert response.json == None

def test_calculator_invalid_zero_input():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna 
        um `ZeroDivisionError` se o valor de `qtd_pessoas` for 0.
    """
    with app_.test_client() as client:
        with pytest.raises(ZeroDivisionError):
            response = client.post('/calculadora/calcular', data={
                'qtd_pessoas': '0',
                'gasto_mensal': '0',
                'estado': 'sudeste'
            })


def test_calculator_valid_upper_limit_input():
    """
        Testa se o `POST` da rota "/calculadora/calcular" retorna o cálculo realizado
        corretamente para valores elevados, resposta com status 200 e JSON contendo as
        chaves 'gasto_agua', 'gasto_pessoa' com valores iguais a 0.
    """
    expected = {
        'gasto_agua': 31699996.83,
        'gasto_pessoa': 333.3333
    }

    with app_.test_client() as client:
        response = client.post('/calculadora/calcular', data={
            'qtd_pessoas': '1000000',
            'gasto_mensal': '9999999',
            'estado': 'sudeste'
        })
    
    assert response.status_code == 200
    assert response.json == expected
