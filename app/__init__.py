# app/__init__.py
from flask import Flask
from app.routes import bp as routes_bp

app = Flask(__name__)
app.template_folder = 'templates'

# 註冊藍圖
app.register_blueprint(routes_bp)
