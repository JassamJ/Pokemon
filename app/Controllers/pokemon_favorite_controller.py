from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.Schemas.p_fav_schema import PokemonFavoriteSchema, ValidationError
from bson import ObjectId
from app.models.factory import modelFactory
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('favorite_pokemons', __name__, url_prefix='/favorite_pokemons')
RM = ResponseManager()
FP_MODEL = modelFactory
FP_SCHEMA = PokemonFavoriteSchema

#crear
@bp.route('/get all', methods=['POST'])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = request.json
        data = FP_SCHEMA.load(data)
        data["user_id"] = user_id
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesaeio enviar todos los parametros")
    
#Eliminar
@bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

#get all
@bp.route("/<string:user_id>", methods=["GET"])
@jwt_required()
def get_all(user_id):
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)