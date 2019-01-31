from back_end.CardData import ALLCARDSJSON
from back_end.Model.Card import Card
from back_end.Model.Filter import Filter
from back_end.Model.Pagination import Pagination

from pprint import pprint

class Cards:
  def __init__(self):
    Cards.setCards(self)
    Cards.resetAccumulator(self)

  def setCards(self):
    self.all_cards = {}

    for cardName, card in ALLCARDSJSON.items():
      newCard = Card(card)
      Cards.bucketFoundCardsWithSameName(self, newCard)

  def bucketFoundCardsWithSameName(self, card):
    if card.name in self.all_cards:
      self.all_cards[card.getName()].append(card)
    else:
      self.all_cards[card.getName()] = [card]

  def getColorFilterFlag(self, queryFilter):
    flag = False
    if len(queryFilter) == 1 and queryFilter[0] == 'True':
      flag = True

    return flag

  def additionalColorFilterConstraints(self, matchExactFilter, matchMultiFilter, excludeFilter):
    matchExact = self.getColorFilterFlag(matchExactFilter)
    matchMulti = self.getColorFilterFlag(matchMultiFilter)
    exclude = self.getColorFilterFlag(excludeFilter)

    if (matchExact == True or exclude == True) and matchMulti == False:
      return True
    elif matchExact == False and exclude == False and matchMulti == True:
      return True
    else:
      return False

  def filterByName(self, queryToFilterOn):
    result = Filter.filterWithName(self.all_cards, queryToFilterOn)
    self.addListToAccumulator(result)

  def filterByTypeAndSubType(self, queryToFilterOn):
    result = Filter.filterWithTypesAndSubTypes(self.all_cards, queryToFilterOn)
    self.addListToAccumulator(result)

  def filterByText(self, queryToFilterOn):
    result = Filter.filterWithText(self.all_cards, queryToFilterOn)
    self.addListToAccumulator(result)

  def filterByColor(self, queryToFilterOn, matchExactFilter, matchMultiFilter, excludeFilter, filteredWithSuperTypes):
    hasAdditionalColorFilterConstraints = self.additionalColorFilterConstraints(matchExactFilter, matchMultiFilter, excludeFilter)

    if hasAdditionalColorFilterConstraints == True:
      matchExactFlag = self.getColorFilterFlag(matchExactFilter)
      matchMultiFlag = self.getColorFilterFlag(matchMultiFilter)
      excludeFlag = self.getColorFilterFlag(excludeFilter)

      result = Filter.filterByColorWithConstraints(self.accumulator, queryToFilterOn, matchExactFlag, matchMultiFlag, excludeFlag)
    else:
      result = Filter.filterByColorNoConstraints(self.accumulator, queryToFilterOn)

    self.resetAccumulator()
    self.addListToAccumulator(result)

  def resetAccumulator(self):
    self.accumulator = {}
    self.found_cards_names_list = []

  def addListToAccumulator(self, listToAdd):
    for cardName, card in listToAdd.items():
      if cardName not in self.found_cards_names_list:
        self.accumulator[cardName] = card
        self.found_cards_names_list.append(cardName)

  def sortAccumulator(self):
    result = []
    self.found_cards_names_list.sort(key=str.lower)

    for name in self.found_cards_names_list:
      result.append(self.accumulator[name])

    return result

  def serialize(self, accumulatedList):
    serializedAccumulator = []

    for card in accumulatedList:
      serializedList = []

      for singleCard in card:
        serializedList.append(singleCard.__dict__)

      serializedAccumulator.append(serializedList)

    return serializedAccumulator

  def search(self, searchParams):
    filteredOnSuperTypes = len(searchParams.getNameFilter()) > 0 or len(searchParams.getTypesFilter()) > 0 or len(searchParams.getCardTextFilter()) > 0

    if filteredOnSuperTypes == True:
        # Filter cards by super type filters first
        self.filterByName(searchParams.getNameFilter())
        self.filterByTypeAndSubType(searchParams.getTypesFilter())
        self.filterByText(searchParams.getCardTextFilter())
    else:
        self.accumulator = self.all_cards

    # Filter accumulated list
    if len(searchParams.getColorFilter()) > 0:
      self.filterByColor(searchParams.getColorFilter(), searchParams.getMatchExactFilter(), searchParams.getMatchMultiFilter(), searchParams.getExcludeFilter(), filteredOnSuperTypes)

    # Sort list pre pagination
    sortedCards = self.sortAccumulator()

    # Paginate list
    paginated = Pagination.paginateResponse(searchParams.getPageFilter(), sortedCards)

    # SerializeResult
    serializeResult = self.serialize(paginated)

    return serializeResult
