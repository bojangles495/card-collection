from flask import Blueprint, request
from operator import itemgetter, attrgetter, methodcaller

from pprint import pprint

from back_end.Model.SearchRequestParams import SearchRequestParams
from back_end.Model.Response import formatResponse
from back_end.Model.Cards import Cards

cards = Blueprint('cards', __name__)
@cards.route('/', methods=['GET'])
def index():
    searchParamFilters = SearchRequestParams(request.args)
    cardsModel = Cards()
    searchResult = cardsModel.search(searchParamFilters)

    return formatResponse(cards, {'cards': searchResult})
