from pprint import pprint

class Filter:
  def hasCardBeenSeen(foundCards, cardName):
    if cardName in foundCards:
      return True
    else:
      return False

  def excludeCard(excludeList, cardColors):
    exclude = False

    for color in excludeList:
      if set(color).issubset(cardColors):
        exclude = True
    return exclude

  def getExclusionList(query):
    all_colors = ['W', 'B', 'U', 'G', 'R']

    for color in query:
      all_colors.remove(color)

    return all_colors



  def filterByColorWithAdditional(query, topLevelFilteredList, match_exactly, match_multi, exclude):
    filteredList = []
    foundIds = set()

    if len(query) > 0:
      if len(topLevelFilteredList) > 0:
        if match_exactly == True and exclude == False:
          filteredList = []
        elif match_exactly == False and exclude == True:
          filteredList = []
        elif match_exactly == True and exclude == True:
          filteredList = []
        elif match_multi == True:
          filteredList = []
        else:
          filteredList = topLevelFilteredList
      else:
        if match_exactly == True and exclude == False:
          for cardName, card in ALLCARDSJSON.items():
            if 'colorIdentity' in card and set(query).issubset(card['colorIdentity']) and card['name'] not in foundIds:
              foundIds.add(card['name'])
              filteredList.append(card)

        elif match_exactly == False and exclude == True:
          exclusion_list = Filter.getExclusionList(query)

          for cardName, card in ALLCARDSJSON.items():
            if 'colors' in card and len(card['colors']) > 0 and len(query) > 0:
              should_exclude = Filter.excludeCard(exclusion_list, card['colors'])

              if should_exclude == False and card['name'] not in foundIds:
                foundIds.add(card['name'])
                filteredList.append(card)

        elif match_exactly == True and exclude == True:
          filteredList = []
        elif match_multi == True:
          filteredList = []
        else:
          filteredList = topLevelFilteredList
    else:
      filteredList = topLevelFilteredList

    return filteredList



#######DONE########
  def filteredWithSuperTypes(nameFilter, typesFilter, textFilter):
    if len(nameFilter) > 0 or len(typesFilter) > 0 or len(textFilter) > 0:
      return True
    else:
      return False

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

  def filterByColorNoConstraints(cardListToFilter, query, filteredWithSuperTypes):
    filteredList = {}
    foundIds = set()
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

            if addCard == True:
              filteredList[cardName] = card

              if cardName not in nameList:
                nameList.append(cardName)

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
        filteredList = []

    # Sort logic
    nameList.sort(key=str.lower)

    sortedFilterList = []
    for name in nameList:
      sortedFilterList.append(filteredList[name])

    return sortedFilterList
