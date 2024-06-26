from flask import Flask
from flasgger import Swagger
from app.routes.main import jwt, cors, main

def create_app():

    app = Flask(__name__)
    Swagger(app)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(main)

    return app