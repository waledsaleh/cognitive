from rest_api_demo.database import db
from rest_api_demo.database.models import Pet,User, Bid

def create_pet(data):
    name = data.get('pet_name')
    pet = Pet(name)
    db.session.add(pet)
    db.session.commit()

def create_bid(data):
    bid_amount = data.get('bid_amount')
    pet_name = data.get('pet_name')
    user_id = data.get('user_id')
    pet = Pet.query.filter(Pet.pet_name == pet_name).one()
    user = User.query.filter(User.id == user_id).one()

    bid = Bid(bid_amount,user,pet)

    db.session.add(bid)
    db.session.commit()
def calculate_lottery(bids):
    bids_dict = {}
    for i in bids:
        bids_dict[i.user.name] = i.bid_amount
    pos = 0
    sorted_dict = sorted(bids_dict.items(), key=lambda x: x[1], reverse=True)
    for i, v in enumerate(sorted_dict):
        if pos < len(sorted_dict)-1:
           bids_dict[sorted_dict[pos][0]] = sorted_dict[pos+1][1]
        pos += 1

    bids_dict = dict(sorted(bids_dict.items(), key=lambda x: x[1]))
    sorted_dict = sorted(bids_dict.items(), key=lambda x: x[1])
    if sorted_dict[0][1] == sorted_dict[1][1]:
        if sorted_dict[0][0] < sorted_dict[1][0]:
              bids_dict[sorted_dict[0][0]] = "Lost"

    return bids_dict
