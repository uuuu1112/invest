from flask import Blueprint
from app.models import *

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return 'Welcome to the main page'

@bp.route('/about')
def about():
    return 'This is the about page'

@bp.route('/test')
def test():
    today=Today()
    return str(today.todayPrice().iloc[-1])
