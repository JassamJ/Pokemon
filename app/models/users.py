from app import mongo

class Users:
    collection = mongo.db.User

    @staticmethod
    def finde_all(User):
        Users = User.collection.find()
        return list(Users)
    
    @staticmethod
    def find_by_id(User_id):
        Users = Users.collection.find_one({
            "_id": User_id
        })
        return Users
    
    @staticmethod
    def create(data):
        User = User.collection.insert_one(data)
        return User.inserted_id
    
    @staticmethod
    def update(User_id, data):
        Users = Users.collection.Update_one({
            "_id": User_id
        }, {
            "$set": data
        })
        return Users

    @staticmethod
    def delete(User_id):
        return Users.collection.delete_one({"_id": User_id})
