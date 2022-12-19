from flask_restx import Api, Resource, fields, Namespace
from flask import Flask, request, jsonify
from models import Participant
from flask_jwt_extended import jwt_required


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

@participant_ns.route('/deleteParticipant/<int:id>')
class Signup(Resource):

    @participant_ns.expect(participant_model)
    @participant_ns.marshal_list_with(participant_model)
    def delete(self, id):
        
        p_to_delete = Participant.query.get_or_404(id)

        p_to_delete.delete()

        return p_to_delete

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
    