import { List, Map, OrderedSet, Record } from 'immutable'

import * as RED_GREEN_TOGGLE_ACTIONS from './actions'
import { default as NAMESPACE } from './namespace'
import { createRedGreenToggleRecord } from './record'

export const reducer = (state, action) => {
  let COMPONENT_ID
  let redGreenToggleState

  if(!action || !action.payload || !action.payload.componentId) {
    COMPONENT_ID = 'default'
  } else {
    COMPONENT_ID = action.payload.componentId
  }

  if(!state.hasIn([NAMESPACE, COMPONENT_ID])) {
    redGreenToggleState = state.setIn([NAMESPACE, COMPONENT_ID], createRedGreenToggleRecord(false))
  } else {
    redGreenToggleState = state
  }

  if (action) {
    switch (action.type) {
      case RED_GREEN_TOGGLE_ACTIONS.UPDATE_RED_GREEN_TOGGLE :
        return redGreenToggleState.updateIn([NAMESPACE, COMPONENT_ID]
                                     , record => record.setIn(['checked'], !record.checked)
                                    )
      default:
        return redGreenToggleState
    }
  }

  return redGreenToggleState
}