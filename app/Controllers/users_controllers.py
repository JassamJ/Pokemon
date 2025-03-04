from flask import Blueprint, request, jsonify
from app.Schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import modelFactory
from bson import ObjectId 
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.tools.encription_manager import EncriptionManager

RM = ResponseManager()
bp = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()
user_model = modelFactory.get_model("users")
EM = EncriptionManager()

@bp.route('/login', methods=["POST"])
def login():
    data = request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return RM.error("Es necesario enviar todas las crendenciales", 400)
    user = user_model.get_by_email_password(email, password)
    if not EM.compare_hashes(password, user["password"]):
        return RM.error("credenciales invalidas")
    return RM.success({"user":user, "token": create_access_token((user["_id"]))})
    
@bp.route("/register", methods=["POST"])
def register():
    try:
        data = user_schema.load(request.json)

    
        data["password"] = EM.create_hash(data["password"])

        user_id = user_model.create(data)
        return RM.success({
            "user_id": str(user_id), 
            "token": create_access_token(str(user_id))
        })

    except ValidationError as err:
        return RM.error("Los parámetros enviados son incorrectos.")

@bp.route('/update', methods=["PUT"])
@jwt_required()
def update():
    user_id = get_jwt_identity()
    try:
        data = user_schema.load(request.json)
        data["password"] = EM.create_hash(data["password"])
        user = user_model.update(ObjectId(user_id), data)
        return RM.success({
            "data" : user
        })
    except ValidationError as err:
        return RM.error("los parametros enviados son incorrectos")
    
@bp.route('/delete', methods=["DELETE"])
@jwt_required()
def delete():
    user_id = get_jwt_identity()
    user_model.delete(ObjectId(user_id))
    return RM.success("Usuario eliminado con exito")

@bp.route('/get', methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = user_model.find_by_id(ObjectId(user_id))
    if not user:
        return RM.error("Usuario no encontrado")
    return RM.success(user)