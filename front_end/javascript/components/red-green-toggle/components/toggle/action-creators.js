import * as RED_GREEN_TOGGLE_ACTIONS from './actions'

export const updateToggle = (componentId) => {
  const action = 
    { type: RED_GREEN_TOGGLE_ACTIONS.UPDATE_RED_GREEN_TOGGLE
    , payload: 
        { 'componentId': !componentId ? 'default' : componentId
        }
    }

  return action
}