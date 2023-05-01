from .app import app as app_

def test_read_main_should_return_status_200():
    with app_.test_client() as client:
        response = client.get("/")
    
    assert response.status_code == 200

def test_graphic_route_exists():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Até 8 anos!"})

    assert response.status_code == 200