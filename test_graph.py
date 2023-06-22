import pytest
from .app import app as app_

def test_graph_mimetype_image():
    """
        Testa se a resposta da rota "/graficos/up_to_16"
        está sendo retornada corretamente como um documento HTML.
    """
    with app_.test_client() as client:
        response = client.get("/graficos/up_to_16")

    assert response.headers['content-type'] == "text/html; charset=utf-8"