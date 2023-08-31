from app import app
# from flask import Flask
# from app.routes import bp as routes_bp

# app = Flask(__name__)
# app.template_folder = 'app/templates'

# # 註冊藍圖
# app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)