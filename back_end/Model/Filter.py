from pprint import pprint
import numpy


class Filter:
  def filteredWithSuperTypes(nameFilter, typesFilter, textFilter):
    return len(nameFilter) > 0 or len(typesFilter) > 0 or len(textFilter) > 0

  def generateSortedListByName(nameList, listToSort):
    result = []
    nameList.sort(key=str.lower)

    for name in nameList:
      result.append(listToSort[name])

    return result

  def addFilteredCard(addCard, cardName, card, nameList, filteredList):
    if addCard == True:
      filteredList[cardName] = card

      if cardName not in nameList:
        nameList.append(cardName)

  def filterWithName(allCards, query):
    filteredCards = []

    if len(query) > 0:
      for cardName, card in allCards.items():
        if cardName.lower().find(query[0].lower()) > -1:
          filteredCards.append(card)

    return filteredCards

  def filterWithTypesAndSubTypes(allCards, query):
    foundCards = set()
    filteredCards = []

    if len(query) > 0:
      query_post_split = query[0].lower().split(" ")

      for cardName, card in allCards.items():
        addCard = False

        for singleCard in card:
          lower_case_types = [element.lower() for element in singleCard.getTypes()]
          lower_case_subtypes = [element.lower() for element in singleCard.getSubtypes()]

          if set(query_post_split).issubset(set(lower_case_types)) or set(query_post_split).issubset(set(lower_case_subtypes)):
            addCard = True

        if addCard == True:
          filteredCards.append(card)

    return filteredCards

  def filterWithText(allCards, query):
    filteredCards = []

    if len(query) > 0:
      for cardName, card in allCards.items():
        addCard = False

        for singleCard in card:
          if singleCard.getText().lower().find(query[0].lower()) > -1:
            addCard = True

        if addCard == True:
          filteredCards.append(card)

    return filteredCards

  def filterExcludeOnlyConstraint(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    nameList = []

    for color in query:
      if filteredWithSuperTypes == True:
        for card in cardListToFilter:
          addCard = False
          currentCardName = ""

          for singleCard in card:
            currentCardName = singleCard.getName()
            singleColorMatch = numpy.array_equal([color], singleCard.getColors())
            multiColorMatch = numpy.array_equal(query, singleCard.getColors())

            if (singleColorMatch == True or (multiColorMatch == True and currentCardName not in nameList)) and addCard != True:
              addCard = True

          Filter.addFilteredCard(addCard, currentCardName, card, nameList, filteredList)
      else:
        for cardName, card in cardListToFilter.items():
          addCard = False

          for singleCard in card:
            singleColorMatch = numpy.array_equal([color], singleCard.getColors())
            multiColorMatch = numpy.array_equal(query, singleCard.getColors())

            if (singleColorMatch == True or (multiColorMatch == True and cardName not in nameList)) and addCard != True:
              addCard = True

          Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return Filter.generateSortedListByName(nameList, filteredList)

  def filterMatchExactConstraint(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    nameList = []

    if filteredWithSuperTypes == True:
      for card in cardListToFilter:
        addCard = False
        foundMatch = False
        currentCardName = ""

        for singleCard in card:
          currentCardName = singleCard.getName()
          if addCard != True:
            foundMatch = all(elem in singleCard.getColors() for elem in query)

            if foundMatch == True:
              addCard = True
        Filter.addFilteredCard(addCard, currentCardName, card, nameList, filteredList)
    else:
      for cardName, card in cardListToFilter.items():
        addCard = False
        foundMatch = False

        for singleCard in card:
          if addCard != True:
            foundMatch = all(elem in singleCard.getColors() for elem in query)

            if foundMatch == True:
              addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return Filter.generateSortedListByName(nameList, filteredList)

  def filterMatchExactAndExcludeConstraint(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    nameList = []

    if filteredWithSuperTypes == True:
      for card in cardListToFilter:
        addCard = False
        currentCardName = ""

        for singleCard in card:
          currentCardName = singleCard.getName()
          multiColorMatch = numpy.array_equal(query, singleCard.getColors())

          if multiColorMatch == True and currentCardName not in nameList and addCard != True:
            addCard = True

        Filter.addFilteredCard(addCard, currentCardName, card, nameList, filteredList)
    else:
      for cardName, card in cardListToFilter.items():
        addCard = False

        for singleCard in card:
          multiColorMatch = numpy.array_equal(query, singleCard.getColors())

          if multiColorMatch == True and cardName not in nameList and addCard != True:
            addCard = True

        Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return Filter.generateSortedListByName(nameList, filteredList)

  def filterMatchMultiColorConstraint(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    nameList = []

    for color in query:
      if filteredWithSuperTypes == True:
        for card in cardListToFilter:
          addCard = False
          currentCardName = ""

          for singleCard in card:
            currentCardName = singleCard.getName()

            if len(singleCard.getColors()) > 1 and addCard != True and currentCardName not in nameList and color in singleCard.getColors():
              addCard = True

          Filter.addFilteredCard(addCard, currentCardName, card, nameList, filteredList)
      else:
        for cardName, card in cardListToFilter.items():
          addCard = False

          for singleCard in card:
            if len(singleCard.getColors()) > 1 and addCard != True and cardName not in nameList and color in singleCard.getColors():
              addCard = True

          Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)

    return Filter.generateSortedListByName(nameList, filteredList)

  def filterByColorWithConstraints(cardListToFilter, query, filteredWithSuperTypes, matchExactFilter, matchMultiFilter, excludeFilter):
    filteredList = {}
    nameList = []

    if len(query) > 0:
      if matchExactFilter == False and excludeFilter == True:
        result = Filter.filterExcludeOnlyConstraint(cardListToFilter, query, filteredWithSuperTypes)
      elif matchExactFilter == True and excludeFilter == False:
        result = Filter.filterMatchExactConstraint(cardListToFilter, query, filteredWithSuperTypes)
      elif matchExactFilter == True and excludeFilter == True:
        result = Filter.filterMatchExactAndExcludeConstraint(cardListToFilter, query, filteredWithSuperTypes)
      elif matchMultiFilter == True:
        result = Filter.filterMatchMultiColorConstraint(cardListToFilter, query, filteredWithSuperTypes)
      else:
        result = []
    else:
      if filteredWithSuperTypes == True:
        for card in cardListToFilter:
          currentCardName = ""
          for singleCard in card:
            currentCardName = singleCard.getName()

          if currentCardName not in nameList:
            nameList.append(currentCardName)
            filteredList[currentCardName] = card
      else:
        filteredList = {}

      result = Filter.generateSortedListByName(nameList, filteredList)

    return result

  def filterByColorNoConstraints(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    nameList = []

    if len(query) > 0:
      for color in query:
        if filteredWithSuperTypes == True:

          for card in cardListToFilter:
            addCard = False
            currentCardName = ""

            for singleCard in card:
              if color in singleCard.getColorIdentity():
                addCard = True
                currentCardName = singleCard.getName()

            if addCard == True:
              filteredList[currentCardName] = card

              if currentCardName not in nameList:
                nameList.append(currentCardName)

        else:

          for cardName, card in cardListToFilter.items():
            addCard = False

            for singleCard in card:
              if color in singleCard.getColorIdentity():
                addCard = True

            Filter.addFilteredCard(addCard, cardName, card, nameList, filteredList)
    else:
      if filteredWithSuperTypes == True:
        for card in cardListToFilter:
          currentCardName = ""

          for singleCard in card:
            currentCardName = singleCard.getName()

          if currentCardName not in nameList:
            nameList.append(currentCardName)
            filteredList[currentCardName] = card

      else:
        filteredList = {}

    sortedArray = Filter.generateSortedListByName(nameList, filteredList)

    return sortedArray
