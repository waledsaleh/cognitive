import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.petstore.business import create_bid,calculate_lottery
from rest_api_demo.api.petstore.serializers import create_bid_with_user, user_with_bids
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Bid, User, Pet
from sqlalchemy import and_

log = logging.getLogger(__name__)

ns = api.namespace('petstore/bids', description='Operations related to petstore')

@ns.route('/')
class BidCollection(Resource):

    @api.response(201, 'Bid successfully created.')
    @api.expect(create_bid_with_user)
    def post(self):
        """
        Creates a new Petstore bid.
        """
        data = request.json
        create_bid(data)
        return None, 201


@ns.route('/<int:user_id>/<string:pet_name>')
@api.response(404, 'Bids not found.')
class BidItem(Resource):

    @api.marshal_with(user_with_bids)
    def get(self, user_id, pet_name):
        bids = Bid.query.join(User).join(Pet).filter(and_(User.id == user_id, Pet.pet_name == pet_name)).all()
        return bids

@ns.route('/<string:pet_name>')
@api.response(404, 'No Winners')
class Lottery(Resource):

    def get(self, pet_name):
        bids = Bid.query.join(User).join(Pet).filter(Pet.pet_name == pet_name).all()
        if len(bids) == 0:
            return None, 404
        result_dict = calculate_lottery(bids)
        return result_dict, 200