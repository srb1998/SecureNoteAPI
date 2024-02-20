from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True)

class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    note = fields.Str(required=True)
    user_id = fields.Int(required=True)
