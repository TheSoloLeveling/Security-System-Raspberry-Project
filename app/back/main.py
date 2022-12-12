from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS
from config import DevConfig


app=Flask(__name__)
app.config.from_object(DevConfig)
api=Api(app,doc='/docs')

CORS(app)

@api.route('/')
class Resource(Resource):
    def get(self):
            return {"message":"Hello Word"}

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