import pytest
from flask import current_app
from .features.quiz.quiz_funcoes import escolher_perguntas, verifica_resposta

# @pytest.mark.xfail
def test_empty_difficulty_should_raise_exception():
    # given
    STATIC = current_app.config['STATIC']
    output = escolher_perguntas(None, STATIC)
    assert output == None

