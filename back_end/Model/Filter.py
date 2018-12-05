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

  def filterWithSection(query, filterType):
    filteredList = set()
    filteredCards = []

    if len(query) > 0:
      for cardName, card in ALLCARDSJSON.items():
        if filterType in card and card[filterType].lower().find(query[0].lower()) > -1 and card['name'] not in filteredList:
          filteredList.add(card['name'])
          filteredCards.append(card)

    return filteredCards

  def filterWithTypesAndSubTypes(query):
    foundCards = set()
    filteredCards = []

    if len(query) > 0:
      query_post_split = query[0].lower().split(" ")
      pprint(query_post_split)

      for cardName, card in ALLCARDSJSON.items():
        if 'types' in card:
          lower_case_types = [element.lower() for element in card['types']]
          if set(query_post_split).issubset(set(lower_case_types)) and card['name'] not in foundCards:
            foundCards.add(card['name'])
            filteredCards.append(card)

        if 'subtypes' in card:
          lower_case_subtypes = [element.lower() for element in card['subtypes']]
          if set(query_post_split).issubset(set(lower_case_subtypes)) and card['name'] not in foundCards:
            foundCards.add(card['name'])
            filteredCards.append(card)

    return filteredCards
