import pytest
from .app import app as app_

def test_read_main_should_return_status_200():
    with app_.test_client() as client:
        response = client.get("/")
    
    assert response.status_code == 200

def test_verify_route_quiz_gerar():
    with app_.test_client() as client:
        response = client.post("/quiz/gerar", data={'Dificuldade': 'Fácil'})
    
    assert response.status_code == 200

def test_verify_route_quiz_responder():
    with app_.test_client() as client:
        response = client.post("/quiz/responder", data={
            'Dificuldade': 'Fácil',
            'Resposta 1': 'a',
            'Resposta 2': 'b',
            'Resposta 3': 'c',
            'Resposta 4': 'd'
            })
    
    assert response.status_code == 200