const { Record } = require('immutable')

const CARD_PROPERTIES =
  [ 'artist'
  , 'borderColor'
  , 'colorIdentity'
  , 'colorIndicator'
  , 'colors'
  , 'convertedManaCost'
  , 'duelDeck'
  , 'faceConvertedManaCost'
  , 'flavorText'
  , 'frameEffect'
  , 'frameVersion'
  , 'hasFoil'
  , 'hasNonFoil'
  , 'isAlternative'
  , 'isFoilOnly'
  , 'isOnlineOnly'
  , 'isOversized'
  , 'isReserved'
  , 'isTimeshifted'
  , 'layout'
  , 'loyalty'
  , 'manaCost'
  , 'multiverseId'
  , 'name'
  , 'names'
  , 'number'
  , 'originalText'
  , 'originalType'
  , 'power'
  , 'printings'
  , 'rarity'
  , 'subtypes'
  , 'supertypes'
  , 'text'
  , 'toughness'
  , 'type'
  , 'types'
  , 'uuid'
  ]

const generateDefaultConfig = () => {
  const config = {}

  CARD_PROPERTIES.forEach(property => {
    config[property] = undefined
  })

  return config
}

const CreateClassRecord = (config) => {
  return Record(config)
}

const Card = class {
  constructor(card) {
    this.DEFAULT_CONFIG = generateDefaultConfig()
    this.CARD_RECORD = CreateClassRecord(this.DEFAULT_CONFIG)
    this.createCardInstance = this.createCardInstance.bind(this)
    this.CARD_INSTANCE = this.createCardInstance(card)
  }

  createCardInstance(card) {
    const INSTANCE_CONFIG = this.DEFAULT_CONFIG

    CARD_PROPERTIES.forEach(property => INSTANCE_CONFIG[property] = card[property])

    const record = new this.CARD_RECORD(INSTANCE_CONFIG)

    return record
  }

  getRecord() {
    return this.CARD_INSTANCE
  }
}