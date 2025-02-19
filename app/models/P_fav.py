from app import mongo
from app.models.super_clase import SuperClase

class PokemonFavorites(SuperClase):
     def __init__(self):
        super().__init__("pokemon_fav")
    
    