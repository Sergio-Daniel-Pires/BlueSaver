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

    model_engine = "text-davinci-003"
    prompt = """
        Você é um especialista global no uso de água, seja nas suas diferentes áreas, tanto na indústria, agricultura quanto no uso domético.
        Não responda perguntas que não estão relacionadas com água e nesses casos diga que não aceita a pergunta. Logo abaixo vem minha perguntas:

        """

    data = request.json
    user_input = data["input"]
    print(user_input)

    prompt += user_input

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0
    )


    response = completion.choices[0].text

    return jsonify({"Resposta": response})