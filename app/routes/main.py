from flask import Blueprint, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import swag_from


main = Blueprint("main", __name__)
jwt = JWTManager()
cors = CORS(resources={r"/*":{"origins":"*"}})


@main.route('/')
@swag_from(methods=['GET'])
def home():
    """
    Vista principal de la Aplicación Flask
    Este endpoint no recibe parámetros, sólo ejecuta funciones integradas.
    ---
    responses:
      200:
        description: Vista Principal
        schema:
          type: object
          properties:
            mensaje:
              type: string
              description: Un mensaje que indica que el servidor está en funcionamiento
    """
    return jsonify({"mensaje": "estamos al aire"}), 200
