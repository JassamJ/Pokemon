from app import mongo

class Pokemon_fav:
    collection = mongo.db.Pokemon_fav

    @staticmethod
    def finde_all():
        Favoritos = Pokemon_fav.collection.find()
        return list(Favoritos)
    
    @staticmethod
    def find_by_id(Favoritos_id):
        pokemons_fav = Pokemon_fav.collection.find_one({
            "_id": Favoritos_id
        })
        return pokemons_fav
    
    @staticmethod
    def create(data):
        Favoritos = Pokemon_fav.collection.insert_one(data)
        return Favoritos.inserted_id
    
    @staticmethod
    def update(Favoritos_id, data):
        Favoritos_id = Pokemon_fav.collection.update_one({
            "_id": Favoritos_id
        }, {
            "$set": data
        })
        return Favoritos_id

    @staticmethod
    def delete(Favoritos_id):
        return Pokemon_fav.collection.delete_one({"_id": Favoritos_id})
