from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.Schemas.p_fav_schema import PokemonFavoriteSchema, ValidationError
from bson import ObjectId
from app.models.p_fav import modelFactory
from bson import ObjectId

bp = Blueprint('favorite_pokemons', __name__, url_prefix='/favorite_pokemons')
RM = ResponseManager()
FP_MODEL = modelFactory
FP_SCHEMA = PokemonFavoriteSchema
#crear
@bp.route('/get all', methods=['POST'])
def create():
    try:
        data = request.json
        data = FP_SCHEMA.validate(data)
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesaeio enviar todos los parametros")
#Eliminar
@bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")
#get all
@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = FP_MODEL.find_all()
    return RM.success(data)