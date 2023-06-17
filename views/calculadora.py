from flask import render_template, make_response, Blueprint

calculadora_bp = Blueprint('calculadora', __name__)

@calculadora_bp.route('/')
def calculadora():
    return make_response(render_template('calculadora.html'), 200)