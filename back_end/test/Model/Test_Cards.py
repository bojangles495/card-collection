orig_import = __import__
class Filter:
  def filterWithName(self):
    pprint("got in this filter")
    return None

from unittest.mock import Mock, MagicMock, patch
from pprint import pprint

from back_end.Model.Filter import Filter
from back_end.Model.Cards import Cards
from back_end.Model.Card import Card

def method_to_use():
  pprint('got in this method')

# BucketFoundCardsWithSameName
class Test_BucketFoundCardsWithSameName:
  def setUp(self, cards_list={}):
    self.cards = Cards(cards_list)

  def tearDown(self):
    self.cards = None

  def withAllCardsEmpty(self):
    cardToAdd = Card({ 'name': 'test card name', 'property1': 'card-property' })
    expected = { 'test card name': [ cardToAdd ] }
    self.setUp()
    self.test_library.assertEqual(self.cards.all_cards, {})
    self.cards.bucketFoundCardsWithSameName(cardToAdd)
    self.test_library.assertEqual(self.cards.all_cards, expected)
    self.tearDown()

  def withAllCardsNotContainingBucketedCard(self):
    existingCard = Card({'name': 'existing-card'})
    cardToAdd = Card({ 'name': 'test card name', 'property1': 'card-property' })
    expected = { 'test card name': [ cardToAdd ], 'existing-card': [existingCard] }
    self.setUp({'existing-card': [existingCard]})
    self.test_library.assertEqual(self.cards.all_cards, {'existing-card': [existingCard]})
    self.cards.bucketFoundCardsWithSameName(cardToAdd)
    self.test_library.assertEqual(self.cards.all_cards, expected)
    self.tearDown()

  def withAllCardsContainingBucketedCard(self):
    existingCard = Card({'name': 'existing-card'})
    firstVersionOfCardAdded = Card({ 'name': 'test card name', 'borderColor': 'white' })
    newVersionOfCardAdded = Card({ 'name': 'test card name', 'borderColor': 'black' })
    all_cards_initial = {'existing-card': [existingCard], 'test card name': [firstVersionOfCardAdded] }
    expected = { 'test card name': [ firstVersionOfCardAdded, newVersionOfCardAdded ], 'existing-card': [existingCard] }

    self.setUp(all_cards_initial)
    self.test_library.assertEqual(self.cards.all_cards, all_cards_initial)
    self.cards.bucketFoundCardsWithSameName(newVersionOfCardAdded)
    self.test_library.assertEqual(self.cards.all_cards, expected)
    self.tearDown()

  def runAllTests(self, test_library):
    self.test_library = test_library
    self.withAllCardsEmpty()
    self.withAllCardsNotContainingBucketedCard()
    self.withAllCardsContainingBucketedCard()

# GetColorFilterFlag
class Test_GetColorFilterFlag:
  def setUp(self):
    self.cards = Cards({})

  def tearDown(self):
    self.cards = None

  def argumentIsNone(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag(None))

  def argumentIsNumber(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag(1))

  def argumentIsEmptyString(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag(''))

  def argumentIsEmptyObject(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag({}))

  def argumentIsEmptyArray(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag([]))

  def argumentIsArrayWithIncorrectElement(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag([None]))
    self.test_library.assertFalse(self.cards.getColorFilterFlag([1]))
    self.test_library.assertFalse(self.cards.getColorFilterFlag(['']))
    self.test_library.assertFalse(self.cards.getColorFilterFlag(['Some Value']))
    self.test_library.assertFalse(self.cards.getColorFilterFlag([{}]))

  def argumentIsArrayWithFalseElement(self):
    self.test_library.assertFalse(self.cards.getColorFilterFlag(['False']))

  def argumentIsArrayWithTrueElement(self):
    self.test_library.assertTrue(self.cards.getColorFilterFlag(['True']))

  def runAllTests(self, test_library):
      self.test_library = test_library
      self.setUp()
      self.argumentIsNone()
      self.argumentIsNumber()
      self.argumentIsEmptyString()
      self.argumentIsEmptyObject()
      self.argumentIsEmptyArray()
      self.argumentIsArrayWithIncorrectElement()
      self.argumentIsArrayWithFalseElement()
      self.argumentIsArrayWithTrueElement()
      self.tearDown()

# AdditionalColorFilterConstraints
class Test_AdditionalColorFilterConstraints:
  def setUp(self):
    self.cards = Cards({})
  def tearDown(self):
    self.cards = None

  def withAllAdditionalConstrainsEmpty(self):
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints())

  def withAllAdditionalConstrainsNonArrays(self):
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(None, None, None))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints('', '', ''))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(1, 1, 1))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints({}, {}, {}))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(False, False, False))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(True, True, True))

  def withAllAdditionalConstrainsAsEmptyArrays(self):
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([], [], []))

  def withAllAdditionalConstrainsAsArraysWithNonStrings(self):
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([None], [None], [None]))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([1], [1], [1]))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([False], [False], [False]))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([True], [True], [True]))
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([{}], [{}], [{}]))

  def withAllAdditionalConstrainsAsArraysWithAllEmptyStrings(self):
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints([''], [''], ['']))

  def withAllAdditionalConstrainsAsArraysWithAllFalsePermutations(self):
    match_exact = 'match_exact'
    match_multi = 'match_multi'
    exclude = 'exclude'
    currentFilters = { match_exact: ['False'], match_multi: ['False'], exclude: ['False'] }
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['False'], match_multi: ['True'], exclude: ['True'] }
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['True'], match_multi: ['True'], exclude: ['False'] }
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['True'], match_multi: ['True'], exclude: ['True'] }
    self.test_library.assertFalse(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))

  def withAllAdditionalConstrainsAsArraysWithAllTruePermutations(self):
    match_exact = 'match_exact'
    match_multi = 'match_multi'
    exclude = 'exclude'
    currentFilters = { match_exact: ['False'], match_multi: ['False'], exclude: ['True'] }
    self.test_library.assertTrue(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['True'], match_multi: ['False'], exclude: ['False'] }
    self.test_library.assertTrue(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['True'], match_multi: ['False'], exclude: ['True'] }
    self.test_library.assertTrue(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))
    currentFilters = { match_exact: ['False'], match_multi: ['True'], exclude: ['False'] }
    self.test_library.assertTrue(self.cards.additionalColorFilterConstraints(currentFilters[match_exact], currentFilters[match_multi], currentFilters[exclude]))

  def runAllTests(self, test_library):
    self.test_library = test_library
    self.setUp()
    self.withAllAdditionalConstrainsEmpty()
    self.withAllAdditionalConstrainsNonArrays()
    self.withAllAdditionalConstrainsAsEmptyArrays()
    self.withAllAdditionalConstrainsAsArraysWithNonStrings()
    self.withAllAdditionalConstrainsAsArraysWithAllEmptyStrings()
    self.withAllAdditionalConstrainsAsArraysWithAllFalsePermutations()
    self.withAllAdditionalConstrainsAsArraysWithAllTruePermutations()


    self.tearDown()

# FilterByName
class Test_FilterByName:
  def setUp(self, cards_list={}):
    self.cards = Cards(cards_list)

  @patch('back_end.Model.Cards.Filter')
  def runNameFilterCallsFilterMethod(self, mock_filter):
    existingCard = Card({'name': 'existing-card'})
    initialCardsList = {'existing-card': [existingCard]}
    cardNameFilter = ['existing-card']
    self.setUp(initialCardsList)
    self.cards.filterByName(None)
    self.test_library.assertTrue(mock_filter.filterWithName.called)
    mock_filter.filterWithName.assert_called_with(initialCardsList, None)

  def tearDown():
    self.cards = None

  def runAllTests(self, test_library):
    self.test_library = test_library
    self.runNameFilterCallsFilterMethod()

# FilterByTypeAndSubType
class Test_FilterByTypeAndSubType:
  def setUp(self, cards_list={}):
    self.cards = Cards(cards_list)

  @patch.object(Filter, 'filterWithTypesAndSubTypes')
  def filterTypeAndSubTypeCallsFilterMethod(self, mock_filter):
    self.setUp({})
    # self.cards.filterByTypeAndSubType(None)
    # self.test_library.assertTrue(mock_filter.filterWithTypesAndSubTypes.called)
    # mock_filter.filterWithTypesAndSubTypes.assert_called_with({}, None)

  def tearDown():
    self.cards = None

  def runAllTests(self, test_library):
    self.test_library = test_library
    self.filterTypeAndSubTypeCallsFilterMethod()

# FilterByText
class Test_FilterByText:
  def setUp(self, cards_list={}):
    self.cards = Cards(cards_list)

  @patch.object(Filter, 'filterWithText')
  def filterByTextCallsFilterMethod(self, mock_filterwithtext):
    expectedReturn = {'test-card': {'name': 'test-card', 'property1': 'some property'}}
    mock_filterwithtext.return_value = expectedReturn
    self.setUp({})
    self.cards.filterByText(None)
    self.test_library.assertTrue(mock_filterwithtext.called)
    mock_filterwithtext.assert_called_with({}, None)
    self.test_library.assertEqual(self.cards.accumulator, expectedReturn)

  def tearDown():
    self.cards = None

  def runAllTests(self, test_library):
    self.test_library = test_library
    self.filterByTextCallsFilterMethod()
