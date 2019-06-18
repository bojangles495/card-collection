import * as SEARCH_FILTER_ACTIONS from './actions'

export const updateInputField = (fieldValue) => {
  const action = 
    { type: SEARCH_FILTER_ACTIONS.UPDATE_INPUT_FIELD
    , payload: 
        { fieldValue }
    }

  return action
}
