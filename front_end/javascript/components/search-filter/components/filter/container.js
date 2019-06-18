import { connect } from 'react-redux'

import { SERVICE_ACTION_CREATORS } from 'services'

import { Filter } from './component'
import { CONSTANTS } from './constants'
import { getRecord } from 'components/red-green-toggle'
import * as temp from 'components/red-green-toggle'
import { updateInputField } from './action-creators'
import { getInputField } from './selectors'

const getCards = (...args) => async dispatch => {
  const getCardsResponse = await service_endpoints.getCards({...args[0]})
}

const mapStateToProps = (state) => {
  const inputField = getInputField(state)
  const nameFilterRecord = getRecord(state, CONSTANTS.CARD_NAME_FILTER)
  const typesFilterRecord = getRecord(state, CONSTANTS.CARD_TYPES_FILTER)
  const textFilterRecord = getRecord(state, CONSTANTS.CARD_TEXT_FILTER)
  const greenManaFilterRecord = getRecord(state, CONSTANTS.GREEN_MANA_FILTER)
  const blueManaFilterRecord = getRecord(state, CONSTANTS.BLUE_MANA_FILTER)
  const redManaFilterRecord = getRecord(state, CONSTANTS.RED_MANA_FILTER)
  const blackManaFilterRecord = getRecord(state, CONSTANTS.BLACK_MANA_FILTER)
  const whiteManaFilterRecord = getRecord(state, CONSTANTS.WHITE_MANA_FILTER)
  const exactFilterRecord = getRecord(state, CONSTANTS.EXACT_FILTER)
  const excludeFilterRecord = getRecord(state, CONSTANTS.EXCLUDE_FILTER)
  const multiFilterRecord = getRecord(state, CONSTANTS.MATCH_MULTI_FILTER)

  const props = 
    { inputField
    , nameFilterRecord
    , typesFilterRecord
    , textFilterRecord
    , greenManaFilterRecord
    , blueManaFilterRecord
    , redManaFilterRecord
    , blackManaFilterRecord
    , whiteManaFilterRecord
    , exactFilterRecord
    , excludeFilterRecord
    , multiFilterRecord
    }

  return props
}

const mapDispatchToProps = 
  { getCards: SERVICE_ACTION_CREATORS.getCards
  , updateInputField
  }

const SearchFilterContainer = connect(mapStateToProps, mapDispatchToProps)(Filter)

export { SearchFilterContainer }
