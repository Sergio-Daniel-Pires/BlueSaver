from flask import Blueprint, render_template

home_bp = Blueprint('home', 'home')

@home_bp.route('/')
def home():
    return render_template('home.html')