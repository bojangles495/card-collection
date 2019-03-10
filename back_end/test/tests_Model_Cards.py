import unittest
from pprint import pprint

from back_end.test.Model.Test_Cards import (
      Test_BucketFoundCardsWithSameName
    , Test_GetColorFilterFlag
    , Test_AdditionalColorFilterConstraints
    , Test_FilterByName
    , Test_FilterByTypeAndSubType
    , Test_FilterByText
)

class CardsTest(unittest.TestCase):
    # def test_BucketFoundCardsWithSameName(self):
    #     bucketTest = Test_BucketFoundCardsWithSameName()
    #     bucketTest.runAllTests(self)

    # def test_GetColorFilter(self):
    #     colorFilterFlagTest = Test_GetColorFilterFlag()
    #     colorFilterFlagTest.runAllTests(self)

    # def test_AdditionalColorFilterConstraints(self):
    #     additionalConstraintsTest = Test_AdditionalColorFilterConstraints()
    #     additionalConstraintsTest.runAllTests(self)

    # def test_FilterByName(self):
    #     filterByNameTest = Test_FilterByName()
    #     filterByNameTest.runAllTests(self)

    def test_FilterByTypeAndSubType(self):
        filterByTypesAndSubTypesTest = Test_FilterByTypeAndSubType()
        filterByTypesAndSubTypesTest.runAllTests(self)

    # def test_FilterByText(self):
    #     filterByTextTest = Test_FilterByText()
    #     filterByTextTest.runAllTests(self)


if __name__ == '__main__':
  unittest.main()

