from pprint import pprint
import math

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

    if len(pageQuery) == 1 and arrayLength > 99:
      if Pagination.check_int(pageQuery[0]):
        defaultBeginIndex = 0
        defaultEndIndex = 99
        maxEndIndex = (math.ceil((arrayLength/100)) * 100) - 1
        maxBeginIndex = maxEndIndex - 99
        currentPage = int(pageQuery[0])

        if currentPage < 2:
          defaultPageBeginIndex = defaultBeginIndex
          defaultPageEndIndex = defaultEndIndex
        else:
          defaultPageBeginIndex = defaultBeginIndex + ((currentPage - 1) * 100)
          defaultPageEndIndex = defaultEndIndex + ((currentPage - 1) * 100)



        if defaultPageBeginIndex > maxEndIndex:
          beginIndex = maxBeginIndex
          endIndex = maxEndIndex
        else:
          beginIndex = defaultPageBeginIndex
          endIndex = defaultPageEndIndex

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
