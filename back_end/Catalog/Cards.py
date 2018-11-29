from flask import Blueprint, request

from pprint import pprint

from back_end.Model.Filter import Filter
from back_end.Model.Response import formatResponse

cards = Blueprint('cards', __name__)

@cards.route('/', methods=['GET'])
def index():
    colorFilter = request.args.getlist("color")
    rangeMinFilter = request.args.getlist("range_min")
    rangeMaxFilter = request.args.getlist("range_max")
    nameFilter = request.args.getlist("name")
    cardTextFilter = request.args.getlist("card_text")

    filteredCardsByName = Filter.filterWithSection(nameFilter, 'name')
    filteredCardsByText = Filter.filterWithSection(cardTextFilter, 'text')

    return formatResponse(cards, {'cards': filteredCardsByName})
