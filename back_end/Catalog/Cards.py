from flask import Blueprint, request
from operator import itemgetter, attrgetter, methodcaller

from pprint import pprint

from back_end.Model.Filter import Filter
from back_end.Model.Response import formatResponse
from back_end.Model.Pagination import Pagination

from back_end.Model.Card import Card
from back_end.Model.Cards import Cards

cards = Blueprint('cards', __name__)
@cards.route('/', methods=['GET'])
def index():
    nameFilter = request.args.getlist("name")
    typesFilter = request.args.getlist("types")
    cardTextFilter = request.args.getlist("card_text")
    colorFilter = request.args.getlist("color")
    colorFilter.sort(key=str.lower)
    matchExactFilter = request.args.getlist("match_exact")
    matchMultiFilter = request.args.getlist("match_multi")
    excludeFilter = request.args.getlist("exclude")
    pageFilter = request.args.getlist("page")

    foundCardNamesList = set()
    initialAccumulator = []

    cardsList = Cards()
    filteredNames = cardsList.filterByName(nameFilter)
    filterTypesAndSubTypes = cardsList.filterByTypeAndSubType(typesFilter)
    filteredText = cardsList.filterByText(cardTextFilter)

    accumulatorList = cardsList.addCardsToAccumulator(initialAccumulator, foundCardNamesList, filteredNames)
    accumulatorList = cardsList.addCardsToAccumulator(accumulatorList, foundCardNamesList, filterTypesAndSubTypes)
    accumulatorList = cardsList.addCardsToAccumulator(accumulatorList, foundCardNamesList, filteredText)

    wasFilterWithSuperTypes = Filter.filteredWithSuperTypes(nameFilter, typesFilter, cardTextFilter)

    filterCardsByColor = cardsList.filterByColor(accumulatorList, colorFilter, matchExactFilter, matchMultiFilter, excludeFilter, wasFilterWithSuperTypes)

    paginated = Pagination.paginateResponse(pageFilter, filterCardsByColor)
    paginatedArray = cardsList.serializeAccumulator(paginated)

    return formatResponse(cards, {'cards': paginatedArray})
