from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from config import DevConfig
from models import User, Participant
from exts import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_required
from participants import participant_ns
from auth import auth_ns
from config import DevConfig, ProdConfig

def create_app():

    app=Flask(__name__)
    
    app.config.from_object(DevConfig)
    
    CORS(app)

    db.init_app(app)

    migrate=Migrate(app,db)

    JWTManager(app)

    api=Api(app,doc='/docs')
    api.add_namespace(participant_ns)
    api.add_namespace(auth_ns)   

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Participant": Participant,
            "User": User
            
        }

    return app




