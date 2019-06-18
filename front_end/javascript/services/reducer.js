import * as ACTIONS from './actions'
import { default as NAMESPACE } from './namespace'
import { createDefaultState } from './record'

export const reducer = (state, action) => {
  let serviceState
  if(!state.get(NAMESPACE)) {
    serviceState = state.set([NAMESPACE], createDefaultState())
  } else {
    serviceState = state
  }

  if (action) {
    switch (action.type) {
      case ACTIONS.SET_SERVICE_STATE :
        return serviceState.setIn([NAMESPACE, 'service-state'], action.payload)
      default:
        return serviceState
    }
  }

  return serviceState
}