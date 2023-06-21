from .app import app as app_

def test_read_main_should_return_status_200():
    with app_.test_client() as client:
        response = client.get("/")
    
    assert response.status_code == 200

def test_verify_route_quiz_gerar():
    with app_.test_client() as client:
        response = client.post("/quiz/", data={'Dificuldade': 'Fácil'})
    
    assert response.status_code == 200

def test_verify_route_quiz_responder():
    with app_.test_client() as client:
        response = client.post("/quiz/", data={
            'Dificuldade': 'Fácil',
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd'
            })
    assert response.status_code == 200
    
def test_graphic_route_exists():
    with app_.test_client() as client:
        response = client.get("/graficos/")
    assert response.status_code == 200

def test_verify_route_graphic_8_years():
    with app_.test_client() as client:
        response = client.get("/graficos/8_old")
    assert response.status_code == 200

def test_verify_route_graphic_9_15_years():
    with app_.test_client() as client:
        response = client.get("/graficos/between_9_and_15")
    assert response.status_code == 200

def test_verify_route_graphic_16_years():
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")
    assert response.status_code == 200
