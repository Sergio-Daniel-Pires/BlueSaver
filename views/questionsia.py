from flask import render_template, make_response, Blueprint, request, jsonify
import os, openai

chatgpt_bp = Blueprint('chatGPT', __name__)

@chatgpt_bp.route('/')
def calculator_page():
    return make_response(render_template('chatgpt.html'), 200)

class ChatGPT:
    def __init__(self, prompt):
        self.prompt = prompt

    
    def get_answer(self):
            model_engine = "text-davinci-003"
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=self.prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0
            )

            response = completion.choices[0].text
            return response
    

@chatgpt_bp.route('/responder', methods=['POST'])
def answer_chatgpt():
    """ 
    Essa função deve receber a perguntas do quiz e devolver o resultado do chatGPT
    """

    prompt = """
        Você é um especialista global no uso de água, seja nas suas diferentes áreas, tanto na indústria, agricultura quanto no uso domético.
        Não responda perguntas que não estão relacionadas com água e nesses casos diga que não aceita a pergunta porque ela deve estar relacionada a água. Logo abaixo vem minha pergunta:

        """

    data = request.json
    user_input = data["input"]
    print(user_input)

    prompt += user_input

    chat = ChatGPT(prompt)
    response = chat.get_answer()

    return jsonify({"Resposta": response})
