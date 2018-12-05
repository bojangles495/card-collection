from pprint import pprint

class Pagination:
  def check_int(s):
    s = str(s)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

  def updateStartIndex(testIndex, verifyValue):
    if testIndex < verifyValue:
      return testIndex
    else:
      newTestIndex = testIndex - 100
      return Pagination.updateStartIndex(newTestIndex, verifyValue)

  def getPaginationIndices(pageQuery, arrayLength):
    beginIndex = 0
    endIndex = 99

    if len(pageQuery) == 1:
      if Pagination.check_int(pageQuery[0]):
        currentPage = int(pageQuery[0])
        endIndex = (currentPage * 100) - 1

        if endIndex > 0:
          beginIndex = endIndex - 99
        else:
          beginIndex = 0
          endIndex = 99

        if beginIndex > arrayLength and arrayLength != 0:
          beginIndex = Pagination.updateStartIndex(beginIndex, arrayLength)
          endIndex = beginIndex + 99
        else:
          beginIndex = 0
          endIndex = 99

    return {'beginIndex': beginIndex, 'endIndex': endIndex}

  def paginateResponse(pageQuery, arrayToPaginate):
    indices = Pagination.getPaginationIndices(pageQuery, len(arrayToPaginate))

    paginateArray = []

    for i in range(indices['beginIndex'], indices['endIndex']+1):
      if i < len(arrayToPaginate):
        paginateArray.append(arrayToPaginate[i])
      else:
        break

    return paginateArray
