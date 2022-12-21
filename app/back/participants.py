from flask_restx import Api, Resource, fields, Namespace
from flask import Flask, request, jsonify
from models import Participant
from flask_jwt_extended import jwt_required
import json
import csv
import os
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np

participant_ns = Namespace('participant', description = "A namespace for participants")

participant_model = participant_ns.model(
    "participant",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "description": fields.String(),
        "photo": fields.String()
    }
)

@participant_ns.route('/createParticipant')
class Signup(Resource):

    @participant_ns.expect(participant_model)
    def post(self):
        data = request.get_json()


        new_user = Participant(
            title = data.get('title'),
            description = data.get('description'),
            photo = data.get('photo')
        )

        new_user.save()

        return jsonify({"message": "Participant created successfuly"})

@participant_ns.route('/increment')
class Signup(Resource):

    def get(self):
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.txt", "r") as f:
            integer = f.read()
        print(integer)
        integer = int(integer)
        integer += 1
        print(integer)
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.txt", "w") as f:
            f.write(str(integer))

        return jsonify({"message": "Unknown variable is inremented"})
    
@participant_ns.route('/getText')
class Signup(Resource):

    def get(self):
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.txt", "r") as f:
            integer = f.read()
        json_data = json.dumps(int(integer))
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.json", "w") as f:
            json.dump(json_data, f)

        return jsonify({"message": integer})

@participant_ns.route('/resetText')
class Signup(Resource):

    def get(self):
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.txt", "w") as f:
            f.write(str(0))

        json_data = json.dumps(int("0"))
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\un.json", "w") as f:
            json.dump(json_data, f)

        return jsonify({"message": "Unknown variable is reset"})


@participant_ns.route('/predict')
class Signup(Resource):

    def post(self):
        data = request.get_json()
        model = tf.keras.models.load_model('model.h5')
        
        new_height = 200
        new_width = 200
        print(data)
        filename = os.path.basename(data)
        folder = r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data'
        link = os.path.join(folder, filename)
        image = Image.open(link)
            
        resized_image = image.resize((new_width, new_height)) 
        resized_image.save(r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\avatar_resized.jpg')

        image = cv2.imread(r'C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\avatar_resized.jpg')

        image = np.array(image,dtype='float32')
        image = image.reshape((-1, 200, 200, 3))

        prediction = model.predict(image).tolist()
        labels = np.array(['anas', 'amina', 'omar', 'Unknown'])
        predictionslabel = np.argmax(prediction)
        label = labels[predictionslabel]

        return jsonify({"predicted label": label}) 


@participant_ns.route('/deleteData')
class Signup(Resource):

    @participant_ns.expect(participant_model)
    def get(self):

        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\data1.json") as data_file:
            data = json.load(data_file)

        [data.pop(0) for item in list(data)]

        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\app\front\src\data\data1.json", "w") as f:
            json.dump(data, f)

        
        with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\SecurityGate\lightTelemetry.csv", 'r') as input_csv:
            reader = csv.reader(input_csv)
            with open(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\SecurityGate\test.csv", 'w', newline='') as output_csv:
                writer = csv.writer(output_csv)
                for i, row in enumerate(reader):
                    if i == 0:
                        writer.writerow(row)
                    else:
                        continue
        input_csv.close()
        output_csv.close()
        os.remove(r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\SecurityGate\lightTelemetry.csv")
        
        old_name = r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\SecurityGate\test.csv"
        new_name = r"C:\Users\bouzi\Desktop\Github\Security-System-Raspberry-Project\SecurityGate\lightTelemetry.csv"

        os.rename(old_name, new_name)

        return jsonify({"message": "Data deleted successfuly"}) 


@participant_ns.route('/participants')
class PartcipantsResource(Resource):

    @participant_ns.marshal_list_with(participant_model)
    def get(self):
        p = Participant.query.all()
        return p

    @participant_ns.marshal_list_with(participant_model)
    @participant_ns.expect(participant_model)
    def post(self):
        data = request.get_json()

        p = Participant(
            title = data.get('title'),
            description = data.get('description'),
            photo = data.get('photo')
        )

        p.save()

        return p, 201

@participant_ns.route('/part/<int:id>')
class PartcipantResource(Resource):

    @participant_ns.marshal_list_with(participant_model)
    def get(self, id):
        p = Participant.query.get_or_404(id)

        return p

    @participant_ns.marshal_list_with(participant_model)
    @jwt_required()
    def put(self, id):
        
        p_to_update = Participant.query.get_or_404(id)

        data = request.get_json()

        p_to_update.update(data.get('title'), data.get('des'))

        return p_to_update

    @participant_ns.marshal_list_with(participant_model)
    def delete(self, id):
        
        p_to_delete = Participant.query.get_or_404(id)

        p_to_delete.delete()

        return p_to_delete


    @participant_ns.marshal_list_with(participant_model)
    def post(self):
        pass
    