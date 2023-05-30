from flask import render_template, make_response
from flask_restx import Namespace, Resource

home_ns = Namespace('home', description='Homepage inicial do Bluesaver')

@home_ns.route('/')
class Homepage(Resource):
    def get(self):
        return make_response(render_template('home.html'), 200)