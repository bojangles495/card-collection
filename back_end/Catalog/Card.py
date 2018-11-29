from flask import Blueprint, request

from pprint import pprint

from back_end.Model.Card import Card
from back_end.Model.Filter import Filter
from back_end.Model.Response import formatResponse

card = Blueprint('card', __name__)

@card.route('/<uuid>', methods=['GET'])
def index(uuid):
  foundCards = Card.getCardByUUID(uuid)

  return formatResponse(card, {'card': foundCards})
