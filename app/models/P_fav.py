from app import mongo
from app.models.super_clase import SuperClase
from bson import ObjectId

class PokemonFavorites(SuperClase):
     def __init__(self):
        super().__init__("pokemon_fav")
    
     def udate(self, object_id, data):
         raise NotImplementedError ("Los pokemones no se pueden actualizar")
     
     def find_by_id(self, object_id):
         raise NotImplementedError("Los pokemones no se pueden encontrar de manera individual")
     
     def finde_all(self, user_id):
         data = self.collection.find({"user_id": ObjectId(user_id)})
         return data