from flask import Blueprint, request, jsonify

bd = Blueprint('pokemons', __name__, url_prefix='/pokemons')