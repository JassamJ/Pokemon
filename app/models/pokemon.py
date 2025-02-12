from app import mongo

class Pokemon:
    collection = mongo.db.pokemon

    @staticmethod
    def finde_all():
        pokemons = Pokemon.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = Pokemon.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon
    
    @staticmethod
    def create(data):
        Pokemon = Pokemon.collection.insert_one(data)
        return Pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon.collection.update_one({
            "_id": pokemon_id
        }, {
            "$set": data
        })
        return pokemon

    @staticmethod
    def delete(pokemon_id):
        return Pokemon.collection.delete_one({"_id": pokemon_id})
