from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from config import DevConfig
from models import User, Participant
from exts import db


app=Flask(__name__)
app.config.from_object(DevConfig)
api=Api(app,doc='/docs')

CORS(app)

db.init_app(app)

participant_model = api.model(
    "participant",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "description": fields.String()
    }
)

@api.route('/')
class Resource(Resource):
    def get(self):
            return {"message":"Hello Word"}

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

    def put(self, id):
        
        p_to_update = Participant.query.get_or_404(id)

        data = request.get_json()

    def delete(self, id):
        pass
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