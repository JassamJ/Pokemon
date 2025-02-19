#se crea
#se elimina
#get all
#modificar la clase del modelo y evitar que se usen metodos indebidos

from flask import Blueprint, request, jsonify
from app.Schemas.p_fav_schema import PokemonFavoriteSchema
from app.models.p_fav import modelFactory
from bson import ObjectId

bd = Blueprint('favorite_pokemons', __name__, url_prefix='/favorite_pokemons')
p_fav_schema = PokemonFavoriteSchema()
p_fav = modelFactory.get_model("pokemon_fav")

@bd.route('/get all', methods=['get'])
def get_all():