from flask import render_template, make_response, Blueprint, url_for, jsonify
from factory import data

dicas_bp = Blueprint("dicas", __name__)

@dicas_bp.route('/', methods=['GET'])
def dicas_page():
    return make_response(render_template('dicas.html'), 200)

@dicas_bp.route('/data', methods=['GET'])
def get_dicas_data():
    all_hints = data.get_all_hints()
    all_hints['place_holder'] = url_for('static', filename=all_hints['place_holder'])
    return jsonify(all_hints)