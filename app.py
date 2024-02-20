from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User_details, Note
from schemas import UserSchema, NoteSchema
import os
from dotenv import load_dotenv

load_dotenv()

# Creating a Flask app
app = Flask(__name__)

# Configuring SQLite database and JWT secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initializing the database
db.init_app(app)
with app.app_context():
    db.create_all()

jwt = JWTManager(app)

# Creating the schemas
user_schema = UserSchema()
note_schema = NoteSchema()

# Creating the routes
@app.route('/signup', methods=['POST'])
def signup():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        if not username or not email or not password:
            return {'message': 'Missing username, email or password'}, 400

        existing_user = User_details.query.filter(
            (User_details.username == username) | (User_details.email == email)
        ).first()

        if existing_user is not None:
            return {'message': 'A user with this username or email already exists'}, 400

        new_user = User_details(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username, 'email': new_user.email}, 201
    except Exception as e: 
        return {'message': str(e)}, 500

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = User_details.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=username)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid username or password'}, 401
    except Exception as e:
        return {'message': str(e)}, 500

@app.route('/notes/create', methods=['POST'])
@jwt_required()
def create_note():
    try:
        note_content = request.json.get('note')
        user_id = get_jwt_identity()

        if not note_content:
            return {'message': 'Note is required'}, 400
        
        new_note = Note(note=note_content, user_id=user_id)
        db.session.add(new_note)
        db.session.commit()

        return {'id': new_note.id, 'note': new_note.note, 'user_id': new_note.user_id}, 201
    except Exception as e:
        return {'message': str(e)}, 500

@app.route('/notes/<int:id>', methods=['GET'])
@jwt_required()
def get_note(id):
    try:
        note = Note.query.get(id)
        if note and note.user_id == get_jwt_identity():
            return {'id': note.id, 'note': note.note, 'user_id': note.user_id}, 200
        else:
            return {'message': 'Note not found or you dont have permission to view it'}, 404
    except Exception as e:
        return {'message': str(e)}, 500

@app.route('/notes/<int:id>', methods=['PUT'])
@jwt_required()
def update_note(id):
    try:
        updated_note = request.json.get('note')

        if not updated_note:
            return {'message': 'Note is required'}, 400
        
        note = Note.query.get(id)
        if note and note.user_id == get_jwt_identity():
            note.note = updated_note
            db.session.commit() 
            return {'id': note.id, 'note': note.note, 'user_id': note.user_id}, 200
        else:
            return {'message': 'Note not found or you dont have permission to update it'}, 404
    
    except Exception as e:
        return {'message': str(e)}, 500

# Running the app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True) 
