from app.models.pokemon import Pokemon
from app.models.P_fav import PokemonFavorites
from app.models.users import Users

class modelFactory:
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": Users,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"La coleccion enviada: {collection_name} no existe")