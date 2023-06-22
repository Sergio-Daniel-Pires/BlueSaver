import pytest
from .app import app as app_

def test_get_content_type_8_years():
    """
        Testa se a resposta da rota "/graficos/8_old"
        está sendo retornada corretamente como um documento HTML.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/8_old")

    assert response.headers['content-type'] == "text/html; charset=utf-8"

def test_get_content_type_9_15_years():
    """
        Testa se a resposta da rota "/graficos/between_9_and_15"
        está sendo retornada corretamente como um documento HTML.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/between_9_and_15")

    assert response.headers['content-type'] == "text/html; charset=utf-8"

def test_get_content_type_16_years():
    """
        Testa se a resposta da rota "/graficos/up_to_16"
        está sendo retornada corretamente como um documento HTML.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")

    assert response.headers['content-type'] == "text/html; charset=utf-8"

@pytest.mark.parametrize("idade_rota", [
    "up_to_1",
    "p_to_16",
    "9_and_15",
    "between_9_and_1",
    "8_oldd",
    "8"
])
def test_get_content_type_invalid_age(idade_rota):
    """
        Testa se a resposta da rota "/graficos/up_to_16"
        está sendo retornada corretamente como um documento HTML.
    """
    caminho = "/graficos/" + idade_rota
    with app_.test_client() as client:
        response = client.get(caminho)

    assert b'Idade invalida, por favor, insira outra e tente novamente' in response.data