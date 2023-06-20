from flask import render_template, make_response, Blueprint, request, jsonify
import os, openai

chatgpt_bp = Blueprint('chatGPT', __name__)

@chatgpt_bp.route('/')
def calculator_page():
    return make_response(render_template('chatgpt.html'), 200)

@chatgpt_bp.route('/responder', methods=['POST'])
def answer_chatgpt():
    """ 
    Essa função deve receber a perguntas do quiz e devolver o resultado do chatGPT
    """
    openai_key = os.environ["OPENAI_API_KEY"]
    model_engine = "text-davinci-003"
    prompt = """
    Você é um especialista global no uso de água, seja nas suas diferentes áreas, tanto na indústria, agricultura quanto no uso domético.
    Não responsa perguntas que não estão relacionadas com água e nesses casos responda sempre a seguinte mensagem:
    Por favor, faça uma pergunta sobre a água.

    """
    print(dict(request.form).get("input", None))
    """
    prompt += request.form["data"]

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0
    )

    response = completion.choices[0].text
    """

    return jsonify({"Resposta": "ddjjk"})