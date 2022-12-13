from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from config import DevConfig
from models import User, Participant
from exts import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config.from_object(DevConfig)
api=Api(app,doc='/docs')

CORS(app)

db.init_app(app)

migrate=Migrate(app,db)

participant_model = api.model(
    "participant",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "description": fields.String()
    }
)

signup_model = api.model(
    "Signup",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String()
    }
)

@api.route('/')
class Resource(Resource):
    def get(self):
            return {"message":"Hello Word"}

@api.route('/signup')
class Signup(Resource):

    @api.expect(signup_model)
    def post(self):
        data = request.get_json()
        username = data.get('username')
        db_user = User.query.filter_by(username=username).first()

        if db_user is not None:
            return jsonify({"message":f"User with username {username} already exists"})

        new_user = User(
            username = data.get('username'),
            email = data.get('email'),
            password = generate_password_hash(data.get('password'))
        )

        new_user.save()

        return jsonify({"message": "User created successfuly"}) 

@api.route('/login')
class Signin(Resource):
    def get(self):
        pass


@api.route('/participants')
class PartcipantsResource(Resource):

    @api.marshal_list_with(participant_model)
    def get(self):
        p = Participant.query.all()
        return p

    @api.marshal_list_with(participant_model)
    def post(self):
        data = request.get_json()

        p = Participant(
            title = data.get('title'),
            description = data.get('description')
        )

        p.save()

        return p, 201

@api.route('/participant/<int:id>')
class PartcipantResource(Resource):

    @api.marshal_list_with(participant_model)
    def get(self, id):
        p = Participant.query.get_or_404(id)

        return p

    @api.marshal_list_with(participant_model)
    def put(self, id):
        
        p_to_update = Participant.query.get_or_404(id)

        data = request.get_json()

        p_to_update.update(data.get('title'), data.get('des'))

        return p_to_update

    @api.marshal_list_with(participant_model)
    def delete(self, id):
        
        p_to_delete = Participant.query.get_or_404(id)

        p_to_delete.delete()

        return p_to_delete


    @api.marshal_list_with(participant_model)
    def post(self):
        pass
    
        

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "Participant": Participant,
        "user":User
        
    }

if __name__ == '__main__':
    app.run()

















def create_app(config):
    app=Flask(__name__)
    app.config.from_object(DevConfig)
    api=Api(app,doc='/docs')

    CORS(app)

    @app.route('/')
    def index():
        return {"message":"Hello Word"}               #app.send_static_file('index.html')

    return app