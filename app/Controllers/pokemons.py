from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.models.pokemon import modelFactory, ValidationError 
from bson import ObjectId

bp = Blueprint('pokemons', __name__, url_prefix='/pokemons')
RM = ResponseManager()
P_MODEL = modelFactory
#crear
@bp.route('/get all', methods=['POST'])
def create():
    try:
        data = request.json
        fp = P_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesaeio enviar todos los parametros")
#Eliminar
@bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    P_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")
#get all
@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = P_MODEL.find_all()
    return RM.success(data)