class SearchRequestParams:
  def __init__(self, requestArguments):
    SearchRequestParams.setNameFilter(self, requestArguments)
    SearchRequestParams.setTypesFilter(self, requestArguments)
    SearchRequestParams.setCardTextFilter(self, requestArguments)
    SearchRequestParams.setColorFilter(self, requestArguments)
    SearchRequestParams.setMatchExactFilter(self, requestArguments)
    SearchRequestParams.setMatchMultiFilter(self, requestArguments)
    SearchRequestParams.setExcludeFilter(self, requestArguments)
    SearchRequestParams.setPageFilter(self, requestArguments)

  # Setters
  def setNameFilter(self, requestArguments):
    self.nameFilter = requestArguments.getlist("name")

  def setTypesFilter(self, requestArguments):
    self.typesFilter = requestArguments.getlist("types")

  def setCardTextFilter(self, requestArguments):
    self.cardTextFilter = requestArguments.getlist("card_text")

  def setColorFilter(self, requestArguments):
    self.colorFilter = requestArguments.getlist("color")
    self.colorFilter.sort(key=str.lower)

  def  setMatchExactFilter(self, requestArguments):
    self.matchExactFilter = requestArguments.getlist("match_exact")

  def setMatchMultiFilter(self, requestArguments):
    self.matchMultiFilter = requestArguments.getlist("match_multi")

  def setExcludeFilter(self, requestArguments):
    self.excludeFilter = requestArguments.getlist("exclude")

  def setPageFilter(self, requestArguments):
    self.pageFilter = requestArguments.getlist("page")

  # Getters
  def getNameFilter(self):
    return self.nameFilter

  def getTypesFilter(self):
    return self.typesFilter

  def getCardTextFilter(self):
    return self.cardTextFilter

  def getColorFilter(self):
    return self.colorFilter


  def getParamFilterValue(self, paramFilter):
    flag = False

    if len(paramFilter) == 1 and paramFilter[0] == 'True':
      flag = True

    return flag

  def getMatchExactFilter(self):
    return self.matchExactFilter

  def getMatchExactFilterValue(self):
    paramFilter = self.getMatchExactFilter()
    return self.getParamFilterValue(paramFilter)

  def getMatchMultiFilter(self):
    return self.matchMultiFilter

  def getExcludeFilter(self):
    return self.excludeFilter

  def getPageFilter(self):
    return self.pageFilter
