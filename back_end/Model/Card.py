import json
from back_end.CardData import ALLCARDSJSON

class Card:
  def getCardByUUID(uuid):
    foundCards = []
    for cardName, card in ALLCARDSJSON.items():
      if 'uuid' in card and card['uuid'] == uuid:
        foundCards.append(card)

    return foundCards

##These are the keys for cards in the json file and the associative type
# artist = string
# borderColor = string
# colorIdentity = array(string)
# colorIndicator = array(string)
# colors = array(string)
# convertedManaCost = float
# flavorText = string
# foreignData = array(object)
#   flavorText = string
#   language = string
#   multiverseId = integer
#   name = string
#   text = string
#   type = string
# frameVersion = string
# hasFoil = bool
# hasNonFoil = bool
# isFoilOnly = bool
# isOnlineOnly = bool
# isOversized = bool
# isReserved = bool
# layout = string
# legalities = object
# loyalty = string
# manaCost = string
# multiverseId = integer
# name = string
# names = array(string)
# number = string
# originalText = string
# originalType = string
# printings = array(string)
# power = string
# rarity = string
# rulings = array(object)
#   date = string
#   text = string
# subtypes = array(string)
# supertypes = array(string)
# text = string
# timeshifted = bool
# toughness = string
# type = string
# types = array(string)
# uuid = string
# watermark = string
