from app import mongo
from app.models.super_clase import SuperClase

class Users(SuperClase):
    def __init__(self):
        super().__init__("users")

    def find_all(self, data):
        raise NotImplementedError("No es necesario obtener todos los usuarios")
    
    def get_by_email_password(self, email, password):
        user = self.collection.fin_one({"email": email, "password": password})
        return user