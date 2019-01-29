from back_end.CardData import ALLCARDSJSON
from back_end.Model.Card import Card
from back_end.Model.Filter import Filter

from pprint import pprint

class Cards:
  def __init__(self):
    Cards.setCards(self)

  def getSortedNamesList(self):
    names = []
    for cardName, card in self.all_cards.items():
      names.append(cardName)

    names.sort(key=str.lower)
    return names

  def generateListSortedByName(self):
    sortedList = {}
    namesList = Cards.getSortedNamesList(self)
    for name in namesList:
      sortedList[name] = self.all_cards[name]

    return sortedList

  def setCards(self):
    self.all_cards = {}

    for cardName, card in ALLCARDSJSON.items():
      newCard = Card(card)
      Cards.bucketFoundCardsWithSameName(self, newCard)

    self.all_cards = Cards.generateListSortedByName(self)

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
    return Filter.filterWithName(self.all_cards, queryToFilterOn)

  def filterByTypeAndSubType(self, queryToFilterOn):
    return Filter.filterWithTypesAndSubTypes(self.all_cards, queryToFilterOn)

  def filterByText(self, queryToFilterOn):
    return Filter.filterWithText(self.all_cards, queryToFilterOn)

  def filterByColor(self, topLevelFilteredList, queryToFilterOn, matchExactFilter, matchMultiFilter, excludeFilter, filteredWithSuperTypes):
    listToFilterWith = self.all_cards

    if filteredWithSuperTypes == True:
      listToFilterWith = topLevelFilteredList

    hasAdditionalColorFilterConstraints = self.additionalColorFilterConstraints(matchExactFilter, matchMultiFilter, excludeFilter)

    if hasAdditionalColorFilterConstraints == True:
      return Filter.filterByColorWithConstraints(listToFilterWith, queryToFilterOn, filteredWithSuperTypes, Cards.getColorFilterFlag(self, matchExactFilter), Cards.getColorFilterFlag(self, matchMultiFilter), Cards.getColorFilterFlag(self, excludeFilter))
    else:
      return Filter.filterByColorNoConstraints(listToFilterWith, queryToFilterOn, filteredWithSuperTypes)

  def addCardsToAccumulator(self, accumulator, foundCardNamesList, listToAdd):
    if len(accumulator) > 0:
      for card in listToAdd:
        addCard = False

        if card[0].getName() not in foundCardNamesList:
          addCard = True
          foundCardNamesList.add(card[0].getName())

        if addCard == True:
          accumulator.append(card)

      return accumulator
    else:
      for card in listToAdd:
        if card[0].getName() not in foundCardNamesList:
          foundCardNamesList.add(card[0].getName())
      return listToAdd

  def serializeAccumulator(self, accumulatedList):
    serializedAccumulator = []

    for card in accumulatedList:
      serializedList = []

      for singleCard in card:
        serializedList.append(singleCard.__dict__)

      serializedAccumulator.append(serializedList)

    return serializedAccumulator
