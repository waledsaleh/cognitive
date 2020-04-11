import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.petstore.business import create_pet
from rest_api_demo.api.petstore.serializers import pet
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Pet

log = logging.getLogger(__name__)

ns = api.namespace('petstore/pets', description='Operations related to petstore')


@ns.route('/')
class PetCollection(Resource):

    @api.marshal_list_with(pet)
    def get(self):
        """
        Returns list of petstore pets.
        """
        pets = Pet.query.all()
        return pets

    @api.response(201, 'Pet successfully created.')
    @api.expect(pet)
    def post(self):
        """
        Creates a new Petstore pet.
        """
        data = request.json
        create_pet(data)
        return None, 201