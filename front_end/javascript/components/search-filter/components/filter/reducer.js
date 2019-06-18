import { List, Map, OrderedSet, Record } from 'immutable'

import * as SEARCH_FILTER_ACTIONS from './actions'
import { default as NAMESPACE } from './namespace'
import { createSearchFilterRecord } from './record'

export const reducer = (state, action) => {
  let searchFilterState

  if(!state.hasIn([NAMESPACE])) {
    searchFilterState = state.setIn([NAMESPACE], createSearchFilterRecord(""))
  } else {
    searchFilterState = state
  }

  if (action) {
    switch (action.type) {
      case SEARCH_FILTER_ACTIONS.UPDATE_INPUT_FIELD :
        return searchFilterState.updateIn([NAMESPACE]
                                     , record => record.setIn(['input-field'], action.payload.fieldValue)
                                    )
      default:
        return searchFilterState
    }
  }

  return searchFilterState
}