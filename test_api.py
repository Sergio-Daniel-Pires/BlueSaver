from .app import app as app_

def test_read_main_should_return_status_200():
    """
        Testa se a resposta da rota home, "/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/")
    
    assert response.status_code == 200

def test_verify_route_chat_gpt_get():
    """
        Testa se a resposta "GET" da rota, "/chatgpt/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get('/chatgpt/')
    
    assert response.status_code == 200

def test_verify_route_quiz_get():
    """
        Testa se a resposta "GET" da rota, "/quiz/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/quiz/")
    
    assert response.status_code == 200

def test_verify_route_calculadora_get():
    """
        Testa se a resposta "GET" da rota, "/calculadora/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/calculadora/")
    
    assert response.status_code == 200

def test_verify_route_quiz_post():
    """
        Testa se a resposta "POST" da rota, "/quiz/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.post("/quiz/")
    
    assert response.status_code == 200
    
def test_graphic_route_exists():
    """
        Testa se a resposta da rota, "/graficos/"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/")
    assert response.status_code == 200

def test_verify_route_graphic_8_years():
    """
        Testa se a resposta da rota, "/graficos/8_old"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/8_old")
    assert response.status_code == 200

def test_verify_route_graphic_9_15_years():
    """
        Testa se a resposta da rota, "/graficos/between_9_and_15"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/between_9_and_15")
    assert response.status_code == 200

def test_verify_route_graphic_16_years():
    """
        Testa se a resposta da rota, "/graficos/up_to_16"
        está sendo retornada corretamente com código 200.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")
    assert response.status_code == 200

def test_invalid_route():
    """
        Testa se a resposta de uma rota inexistente, "/graficos/18_old"
        está sendo retornada corretamente com código 400.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/18_old")

    assert response.status_code == 400
