from flask import Blueprint, request, jsonify
from app.Schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.users import modelFactory
from bson import ObjectId

bp = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()
user_model = modelFactory.get_model("users")

@bp.route('/login', methods=['POST'])
def login():
    data =request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return jsonify("Es necesario enviar")
    user = user_model.get_by_email_password(email, password)
    if not user:
        return jsonify("No se encontro un usuario")
    return jsonify(user, 200)

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = user_schema.load(request.json)
        user_id = user_model.create(data)
        return jsonify({"user_id":str(user_id)}, 200)
    except -ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    
@bp.route('/update/<str:user_id>', methods=['PUT'])
def update(user_id):
    try:
        data = user_schema.load(request.json)
        user = user_model.update(ObjectId(user_id), data)
        return jsonify({
            "data" : user,
        }, 200)
    except -ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    
@bp.route('/delete/<str:user_id>', methods=['DELETE'])
def delete(user_id):
    user_model.delete(ObjectId(user_id))
    return jsonify("Usuario eliminado", 200)
