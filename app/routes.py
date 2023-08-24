# app/routes.py
from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return 'Welcome to the main page'

@bp.route('/about')
def about():
    return 'This is the about page'
