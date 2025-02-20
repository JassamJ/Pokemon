from flask import Blueprint, request, jsonify
from app.Schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.users import modelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager

RM = ResponseManager()
bp = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()
user_model = modelFactory.get_model("users")

@bp.route('/login', methods=['POST'])
def login():
    data =request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return RM.error("Es necesario enviar")
    user = user_model.get_by_email_password(email, password)
    if not user:
        return RM.error("No se encontro un usuario")
    return RM.success(user)

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = user_schema.load(request.json)
        user_id = user_model.create(data)
        return RM.success({"user_id":str(user_id)})
    except -ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route('/update/<str:user_id>', methods=['PUT'])
def update(user_id):
    try:
        data = user_schema.load(request.json)
        user = user_model.update(ObjectId(user_id), data)
        return RM.success({
            "data" : user,
        })
    except -ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route('/delete/<str:user_id>', methods=['DELETE'])
def delete(user_id):
    user_model.delete(ObjectId(user_id))
    return RM.success("Usuario eliminado")

@bd.route("/get/</string:user_id>", methods=["GET"])
def get_user(user:id):
    user = user_model.find_by_id(ObjectId(user_id))
    return RM.success(user)
