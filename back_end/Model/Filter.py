from back_end.CardData import ALLCARDSJSON
from pprint import pprint

class Filter:
  def filterByColor(colors):
    filteredList = []
    foundIds = set()

    if len(colors) > 0:
      for color in colors:
        for cardName, card in ALLCARDSJSON.items():
          if 'colorIdentity' in card and color in card['colorIdentity'] and card['name'] not in foundIds:
            foundIds.add(card['name'])
            filteredList.append(card)

    return filteredList

  def filterByName(names):
    filteredList = set()
    filteredCards = []

    for cardName, card in ALLCARDSJSON.items():
      if 'name' in card and card['name'].lower().find(names[0].lower()) > -1 and card['name'] not in filteredList:
        filteredList.add(card['name'])
        filteredCards.append(card)

    return filteredCards


  def filterWithSection(query, filterType):
    filteredList = set()
    filteredCards = []

    if len(query) > 0:
      for cardName, card in ALLCARDSJSON.items():
        if filterType in card and card[filterType].lower().find(query[0].lower()) > -1 and card['name'] not in filteredList:
          filteredList.add(card['name'])
          filteredCards.append(card)

    return filteredCards
