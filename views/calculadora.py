from flask import render_template, make_response, Blueprint, request, jsonify
from utils.calculadora_funcoes import calcular_valor

calculadora_bp = Blueprint('calculadora', __name__)

@calculadora_bp.route('/')
def calculator_page():
    return make_response(render_template('calculadora.html'), 200)

@calculadora_bp.route('/calcular', methods=['POST'])
def calculator():
    formulario = dict(request.form)
    qtd_pessoas = formulario.get('qtd_pessoas', None)
    gasto_mensal = formulario.get('gasto_mensal', None)
    estado = formulario.get('estado', None)

    if None in (qtd_pessoas, gasto_mensal, estado):
        return "Preencha os dados corretamente!", 400
    if not qtd_pessoas.isalnum() or not gasto_mensal.isalnum():
        return "Os dados precisam ser inteiros validos!", 400
    
    qtd_pessoas = int(qtd_pessoas)
    gasto_mensal = int(gasto_mensal)

    resultados = calcular_valor(qtd_pessoas, gasto_mensal, estado)
    return jsonify(resultados)