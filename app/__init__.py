# app/__init__.py
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'betrue_secret_key'  # 设置secret_key
app.template_folder = 'templates'

# 設定資料庫連接URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# 建立SQLAlchemy實例並綁定到Flask應用程式
# db = SQLAlchemy(app)

from app.routes import bp as routes_bp
# 註冊藍圖
app.register_blueprint(routes_bp)
