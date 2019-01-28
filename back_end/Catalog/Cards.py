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
    matchExactFilter = request.args.getlist("match_exact")
    matchMultiFilter = request.args.getlist("match_multi")
    excludeFilter = request.args.getlist("exclude")
    pageFilter = request.args.getlist("page")

    # match_exact = request.args.getlist("match_exact")
    # match_multi = request.args.getlist("match_multi")
    # exclude = request.args.getlist("exclude")

    # me_flag = getColorFilterFlag(match_exact)
    # mm_flag = getColorFilterFlag(match_multi)
    # ex_flag = getColorFilterFlag(exclude)
    # additionalColorFilterIsValid = additionalColorFilterValidity(me_flag, ex_flag, mm_flag)


    # filteredCardsByName = Filter.filterWithSection(nameFilter, 'name')
    # filteredCardsByTypeAndSubType = Filter.filterWithTypesAndSubTypes(typesFilter)
    # filteredCardsByText = Filter.filterWithSection(cardTextFilter, 'text')

    # filteredListPrePagination = []
    # foundCardsPrePagination = set()

    # appendCardLists(filteredCardsByName, filteredListPrePagination, foundCardsPrePagination)
    # appendCardLists(filteredCardsByTypeAndSubType, filteredListPrePagination, foundCardsPrePagination)
    # appendCardLists(filteredCardsByText, filteredListPrePagination, foundCardsPrePagination)

    # if additionalColorFilterIsValid == True:
    #   temp = Filter.filterByColorWithAdditional(colorFilter, filteredListPrePagination, me_flag, mm_flag, ex_flag)
    #   # pprint(len(temp))
    #   filteredCardsByColor = []

    # else:
    #   filteredCardsByColor = Filter.filterByColorNoAdditional(colorFilter, filteredListPrePagination)
    #   filteredCardsByColor = sorted(filteredCardsByColor, key=itemgetter('name'))

    # paginatedArray = Pagination.paginateResponse(pageFilter, filteredCardsByColor)



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
