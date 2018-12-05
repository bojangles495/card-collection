from flask import Blueprint, request

from pprint import pprint

from back_end.Model.Filter import Filter
from back_end.Model.Response import formatResponse
from back_end.Model.Pagination import Pagination


def appendCardLists(cardsToAddList, prePaginationList, foundCardsList):
  for card in cardsToAddList:
    if card['name'] not in foundCardsList:
        prePaginationList.append(card)
        foundCardsList.add(card['name'])

cards = Blueprint('cards', __name__)

@cards.route('/', methods=['GET'])
def index():
    nameFilter = request.args.getlist("name")
    typesFilter = request.args.getlist("types")
    cardTextFilter = request.args.getlist("card_text")
    colorFilter = request.args.getlist("color")
    pageFilter = request.args.getlist("page")

    filteredCardsByName = Filter.filterWithSection(nameFilter, 'name')
    filteredCardsByTypeAndSubType = Filter.filterWithTypesAndSubTypes(typesFilter)
    filteredCardsByText = Filter.filterWithSection(cardTextFilter, 'text')

    filteredListPrePagination = []
    foundCardsPrePagination = set()

    appendCardLists(filteredCardsByName, filteredListPrePagination, foundCardsPrePagination)
    appendCardLists(filteredCardsByTypeAndSubType, filteredListPrePagination, foundCardsPrePagination)
    appendCardLists(filteredCardsByText, filteredListPrePagination, foundCardsPrePagination)

    paginatedArray = Pagination.paginateResponse(pageFilter, filteredListPrePagination)

    return formatResponse(cards, {'cards': paginatedArray})
