import json
from back_end.CardData import ALLCARDSJSON

class Card:
  def __init__(self, card):
    Card.setArtist(self, card)
    Card.setBorderColor(self, card)
    Card.setColorIdentity(self, card)
    Card.setColorIndicator(self, card)
    Card.setColors(self, card)
    Card.setConvertedManaCost(self, card)
    Card.setDuelDeck(self, card)
    Card.setFaceConvertedManaCost(self, card)
    Card.setFlavorText(self, card)
    Card.setFrameEffect(self, card)
    Card.setFrameVersion(self, card)
    Card.setHasFoil(self, card)
    Card.setHasNonFoil(self, card)
    Card.setIsAlternative(self, card)
    Card.setIsFoilOnly(self, card)
    Card.setIsOnlineOnly(self, card)
    Card.setIsOversized(self, card)
    Card.setIsReserved(self, card)
    Card.setIsTimeshifted(self, card)
    Card.setLayout(self, card)
    Card.setLoyalty(self, card)
    Card.setManaCost(self, card)
    Card.setMultiverseId(self, card)
    Card.setName(self, card)
    Card.setNames(self, card)
    Card.setNumber(self, card)
    Card.setOriginalText(self, card)
    Card.setOriginalType(self, card)
    Card.setPrintings(self, card)
    Card.setPower(self, card)
    Card.setRarity(self, card)
    Card.setSubTypes(self, card)
    Card.setSuperTypes(self, card)
    Card.setText(self, card)
    Card.setToughness(self, card)
    Card.setType(self, card)
    Card.setTypes(self, card)
    Card.setUUID(self, card)

  # Name of artist.
  def setArtist(self, card):
    if 'artist' in card:
      self.artist = card['artist']
    else:
      self.artist = ""

  # Color of the border. Can be black, borderless, gold, silver, or white.
  def setBorderColor(self, card):
    if 'borderColor' in card:
      self.borderColor = card['borderColor']
    else:
      self.borderColor = ""

  # List of all colors in card’s mana cost, rules text and any color indicator.
  def setColorIdentity(self, card):
    if 'colorIdentity' in card:
      self.colorIdentity = card['colorIdentity']
    else:
      self.colorIdentity = []

  # List of all colors in card’s color indicator (a symbol showing the colors of the card).
  # Usually found only on cards without mana costs and other special cards.
  def setColorIndicator(self, card):
    if 'colorIndicator' in card:
      self.colorIndicator = card['colorIndicator']
    else:
      self.colorIndicator = []

  # List of all colors in card’s mana cost and any color indicator. Some cards are special
  # (such as Devoid cards or other cards with certain rules text).
  def setColors(self, card):
    if 'colors' in card:
      self.colors = card['colors']
      self.colors.sort(key=str.lower)
    else:
      self.colors = []

  # The converted mana cost of the card.
  def setConvertedManaCost(self, card):
    if 'convertedManaCost' in card:
      self.convertedManaCost = float(card['convertedManaCost'])
    else:
      self.convertedManaCost = float()

  # If the card is in a duel deck product, can be a or b.
  # (If not in duel deck product, duelDeck is usually ommitted.)
  def setDuelDeck(self, card):
    if 'duelDeck' in card:
      self.duelDeck = card['duelDeck']
    else:
      self.duelDeck = ""

  # The converted mana cost of the face (half, or part) of the card.
  def setFaceConvertedManaCost(self, card):
    if 'faceConvertedManaCost' in card:
      self.faceConvertedManaCost = float(card['faceConvertedManaCost'])
    else:
      self.faceConvertedManaCost = float()

  # Italicized text found below the rules text that has no game function.
  def setFlavorText(self, card):
    if 'flavorText' in card:
      self.flavorText = card['flavorText']
    else:
      self.flavorText = ""

  # Effect found on the card frame style. Can be legendary, miracle, nyxtouched,
  # draft, devoid, tombstone, colorshifted, sunmoondfc, compasslanddfc, originpwdfc, or mooneldrazidfc.
  # (If none, it is usually omitted.)
  def setFrameEffect(self, card):
    if 'frameEffect' in card:
      self.frameEffect = card['frameEffect']
    else:
      self.frameEffect = ""

  # Version of the card frame style. Can be 1993, 1997, 2003, 2015, or future.
  def setFrameVersion(self, card):
    if 'frameVersion' in card:
      self.frameVersion = card['frameVersion']
    else:
      self.frameVersion = ""

  # Can the card be found in foil? Can be true or false. (If false, it is usually omitted.)
  def setHasFoil(self, card):
    if 'hasFoil' in card:
      self.hasFoil = card['hasFoil']
    else:
      self.hasFoil = False

  # Can the card be found in non-foil? Can be true or false. (If false, it is usually omitted.)
  def setHasNonFoil(self, card):
    if 'hasNonFoil' in card:
      self.hasNonFoil = card['hasNonFoil']
    else:
      self.hasNonFoil = False

  # Is the card a "secret foil" in the set? This is a feature found in sets such as UNH, 10E, CN2, BBD, and PLS.
  # Can be true or false. (If false, it is usually omitted.)
  def setIsAlternative(self, card):
    if 'isAlternative' in card:
      self.isAlternative = card['isAlternative']
    else:
      self.isAlternative = False

  # Can the card only be found in foil? Can be true or false. (If false, it is usually omitted.)
  def setIsFoilOnly(self, card):
    if 'isFoilOnly' in card:
      self.isFoilOnly = card['isFoilOnly']
    else:
      self.isFoilOnly = False

  # Is the card only available online? Can be true or false. (If false, it is usually omitted.)
  def setIsOnlineOnly(self, card):
    if 'isOnlineOnly' in card:
      self.isOnlineOnly = card['isOnlineOnly']
    else:
      self.isOnlineOnly = False

  # Is the card oversized? Can be true or false. (If false, it is usually omitted.)
  def setIsOversized(self, card):
    if 'isOversized' in card:
      self.isOversized = card['isOversized']
    else:
      self.isOversized = False

  # Is the card on the Reserved List? Can be true or false. (If false, isReserved is usually omitted.)
  def setIsReserved(self, card):
    if 'isReserved' in card:
      self.isReserved = card['isReserved']
    else:
      self.isReserved = False

  # Card is “timeshifted”, a feature from Time Spiral block.
  # Can be true or false. (If false, it is usually omitted.)
  def setIsTimeshifted(self, card):
    if 'isTimeshifted' in card:
      self.isTimeshifted = card['isTimeshifted']
    else:
      self.isTimeshifted = False

  # The card layout. Possible values: normal, split, flip, double-faced,
  # token, plane, scheme, phenomenon, leveler, vanguard, meld
  def setLayout(self, card):
    if 'layout' in card:
      self.layout = card['layout']
    else:
      self.layout = ""

  # Planeswalker loyalty value.
  def setLoyalty(self, card):
    if 'loyalty' in card:
      self.loyalty = card['loyalty']
    else:
      self.loyalty = ""

  # The mana cost of this card. Consists of one or more mana symbols.
  def setManaCost(self, card):
    if 'manaCost' in card:
      self.manaCost = card['manaCost']
    else:
      self.manaCost = ""

  # An integer most cards have which Wizards uses as a card identifier.
  def setMultiverseId(self, card):
    if 'multiverseId' in card:
      self.multiverseId = card['multiverseId']
    else:
      self.multiverseId = ""

  # The card name. For split, double-faced and flip cards,
  # just the name of one side of the card.
  # Basically each 'sub-card' has its own record.
  def setName(self, card):
    if 'name' in card:
      self.name = card['name']
    else:
      self.name = ""

  # Only used for split, flip, double-faced, and meld cards.
  # Will contain all the names on this card, front or back.
  # For meld cards, the first name is the card with the meld ability,
  # which has the top half on its back, the second name is the card with
  # the reminder text, and the third name is the melded back face.
  def setNames(self, card):
    if 'names' in card:
      self.names = card['names']
    else:
      self.names = []

  # Number of the card.
  def setNumber(self, card):
    if 'number' in card:
      self.number = card['number']
    else:
      self.number = ""

  # Text on the card as originally printed.
  def setOriginalText(self, card):
    if 'originalText' in card:
      self.originalText = card['originalText']
    else:
      self.originalText = ""

  # Type as originally printed. Includes any supertypes and subtypes.
  def setOriginalType(self, card):
    if 'originalType' in card:
      self.originalType = card['originalType']
    else:
      self.originalType = ""

  # List of sets the card was printed in, in uppercase.
  def setPrintings(self, card):
    if 'printings' in card:
      self.printings = card['printings']
    else:
      self.printings = []

  # Power of the creature.
  def setPower(self, card):
    if 'power' in card:
      self.power = card['power']
    else:
      self.power = ""

  # Rarity. Can be basic, common, uncommon, rare, or mythic
  def setRarity(self, card):
    if 'rarity' in card:
      self.rarity = card['rarity']
    else:
      self.rarity = ""

  # What appears to the right of the dash in a card type.
  # Usually each word is its own subtype.
  # Example values: Trap, Arcane, Equipment, Aura, Human, Rat, Squirrel, etc.
  def setSubTypes(self, card):
    if 'subtypes' in card:
      self.subtypes = card['subtypes']
    else:
      self.subtypes = []

  # List of card supertypes found before em-dash.
  def setSuperTypes(self, card):
    if 'supertypes' in card:
      self.supertypes = card['supertypes']
    else:
      self.supertypes = []

  # The text of the card. May contain mana symbols and other symbols.
  def setText(self, card):
    if 'text' in card:
      self.text = card['text']
    else:
      self.text = ""

  # Toughness of the card.
  def setToughness(self, card):
    if 'toughness' in card:
      self.toughness = card['toughness']
    else:
      self.toughness = ""

  # Type of the card. Includes any supertypes and subtypes.
  def setType(self, card):
    if 'type' in card:
      self.type = card['type']
    else:
      self.type = ""

  # What appear to the left of the dash in a card type.
  # Example values: Instant, Sorcery, Artifact, Creature, Enchantment, Land, Planeswalker
  def setTypes(self, card):
    if 'types' in card:
      self.types = card['types']
    else:
      self.types = []

  # A universal unique id (v5) generated by MTGJSON. Each entry is unique.
  def setUUID(self, card):
    if 'uuid' in card:
      self.uuid = card['uuid']
    else:
      self.uuid = ""


  def getColors(self):
    return self.colors

  def getColorIdentity(self):
    return self.colorIdentity

  def getColorIndicator(self):
    return self.colorIndicator

  def getName(self):
    return self.name

  def getSubtypes(self):
    return self.subtypes

  def getText(self):
    return self.text

  def getTypes(self):
    return self.types

  def getUUID(self):
    return self.uuid

  def getCardByUUID(uuid):
    foundCards = []
    for cardName, card in ALLCARDSJSON.items():
      if 'uuid' in card and card['uuid'] == uuid:
        foundCards.append(card)

    return foundCards
