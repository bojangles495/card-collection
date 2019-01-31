from pprint import pprint
import numpy

class Filter:
  def addFilteredCard(addCard, cardName, card, nameList, filteredList):
    if addCard == True:
      filteredList[cardName] = card

      if cardName not in nameList:
        nameList.append(cardName)

  def filterWithName(allCards, query):
    filteredList = {}
    nameList = []

    if len(query) > 0:
      for cardName, card in allCards.items():
        addCard = False

        if cardName.lower().find(query[0].lower()) > -1:
          addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return filteredList

  def filterWithTypesAndSubTypes(allCards, query):
    filteredList = {}
    nameList = []

    if len(query) > 0:
      query_post_split = query[0].lower().split(" ")

      for cardName, card in allCards.items():
        addCard = False

        for singleCard in card:
          lower_case_types = [element.lower() for element in singleCard.getTypes()]
          lower_case_subtypes = [element.lower() for element in singleCard.getSubtypes()]

          if set(query_post_split).issubset(set(lower_case_types)) or set(query_post_split).issubset(set(lower_case_subtypes)):
            addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return filteredList

  def filterWithText(allCards, query):
    filteredList = {}
    nameList = []

    if len(query) > 0:
      for cardName, card in allCards.items():
        addCard = False

        for singleCard in card:
          if singleCard.getText().lower().find(query[0].lower()) > -1:
            addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return filteredList

  def excludeFilterCheck(cardName, card, nameList, query, singleColor):
    singleColorMatch = numpy.array_equal([singleColor], card.getColors())
    multiColorMatch = numpy.array_equal(query, card.getColors())

    return (singleColorMatch == True or (multiColorMatch == True and cardName not in nameList))

  def matchExactFilterCheck(cardName, card, nameList, query, singleColor):
    return (all(elem in card.getColors() for elem in query) and cardName not in nameList)

  def matchExactAndExcludeFilterCheck(cardName, card, nameList, query, singleColor):
    multiColorMatch = numpy.array_equal(query, card.getColors())

    return (multiColorMatch == True and cardName not in nameList)

  def matchMultiFilterCheck(cardName, card, nameList, query, singleColor):
    return (len(card.getColors()) > 1 and singleColor in card.getColors() and cardName not in nameList)

  def filteringWithConstraint(cardListToFilter, query, checkConstraintFilter):
    filteredList = {}
    nameList = []

    for color in query:
      for cardName, card in cardListToFilter.items():
        addCard = False

        for singleCard in card:
          if addCard != True:
            addCard = checkConstraintFilter(cardName, singleCard, nameList, query, color)

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return filteredList

  def filterByColorWithConstraints(cardListToFilter, query, matchExactFilter, matchMultiFilter, excludeFilter):
    if matchExactFilter == False and excludeFilter == True:
      result = Filter.filteringWithConstraint(cardListToFilter, query, Filter.excludeFilterCheck)
    elif matchExactFilter == True and excludeFilter == False:
      result = Filter.filteringWithConstraint(cardListToFilter, query, Filter.matchExactFilterCheck)
    elif matchExactFilter == True and excludeFilter == True:
      result = Filter.filteringWithConstraint(cardListToFilter, query, Filter.matchExactAndExcludeFilterCheck)
    elif matchMultiFilter == True:
      result = Filter.filteringWithConstraint(cardListToFilter, query, Filter.matchMultiFilterCheck)
    else:
      result = []

    return result

  def filterByColorNoConstraints(cardListToFilter, query):
    filteredList = {}
    nameList = []

    for color in query:
      for cardName, card in cardListToFilter.items():
        addCard = False

        for singleCard in card:
          if color in singleCard.getColorIdentity():
            addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return filteredList
