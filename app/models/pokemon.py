from app import mongo
from app.models.super_clase import SuperClase
from bson import ObjectId

class Pokemon(SuperClase):
    def __init__(self):
        super().__init__("pokemons")
    
    def create(self, data):
        raise NotImplementedError("Los pokemons no se pueden crear")
    
    def create(self, object_id):
        raise NotImplementedError("Los pokemons no se pueden eliminar")
    
    def update(self, object_id, data):
        raise NotImplementedError("Los pokemons no se pueden actualizar")
    