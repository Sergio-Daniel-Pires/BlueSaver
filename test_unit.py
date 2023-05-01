from .app import app as app_

def test_route_8_years():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Até 8 anos!"})

    assert response.status_code == 200

def test_route_9_to_15():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Entre 9 e 15!"})

    assert response.status_code == 200

def test_route_up_to_16():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "16 ou mais!"})

    assert response.status_code == 200

def test_mimetype_image():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "16 ou mais!"})

    assert response.headers['content-type'] == "image/png"

def test_no_parameter_idade():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar")

    assert response.status_code == 400

def test_invalid_parameter_idade():
    with app_.test_client() as client:
        response = client.post("/graficos/visualizar", data={"Idade": "Corta pra 18"})

    assert response.status_code == 400