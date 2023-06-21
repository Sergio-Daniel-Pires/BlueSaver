from flask import render_template, make_response, Blueprint, current_app

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return make_response(render_template('home.html'), 200)