from flask_restplus import fields
from rest_api_demo.api.restplus import api

pet = api.model('petstore pet', {
    'pet_name': fields.String(attribute='pet.pet_name'),
})
bid = api.inherit('petstore bid', pet, {
    'bid_amount': fields.Integer(required=True, description='bid amount'),
    'user_name': fields.String(attribute='user.name'),
})

create_bid_with_user = api.model('petstore bid', {
    'bid_amount': fields.Integer(required=True, description='bid amount'),
    'user_id': fields.Integer(required=True, description='user id'),
    'pet_name': fields.String(required=True, description='pet name'),

})

user_with_bids = api.inherit('bids category with user', pet, bid, {
})

