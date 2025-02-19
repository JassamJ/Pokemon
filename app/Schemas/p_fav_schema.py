#id
from marshmallow import Schema, fields, ValidationError

class PokemonFavoriteSchema(Schema):
    pokemon_id = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={"required": "El id es requerido"})
    
    user_id = fields.String(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={"required": "el usuario es requerido"})