from flask import Flask
from flask_restx import Api, Resource
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