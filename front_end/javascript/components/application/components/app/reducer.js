import { Record } from 'immutable'

import * as APPLICATION_ACTIONS from './actions'
import { default as NAMESPACE } from './namespace'
import { createDefaultApplicationRecord } from './record'

export const reducer = (state, action) => {
  let appState
  if(!state.get(NAMESPACE)) {
    appState = state.set([NAMESPACE], createDefaultApplicationRecord())
  } else {
    appState = state
  }

  if (action) {
    switch (action.type) {
      case APPLICATION_ACTIONS.SET_CLICK_HERE :
        return appState.setIn([NAMESPACE, 'set-clicker'], action.payload)
      case APPLICATION_ACTIONS.SET_CLICK_HERE_TWO :
        return appState.setIn([NAMESPACE, 'set-clicker-two'], action.payload)
      default:
        return appState
    }
  }

  return appState
}