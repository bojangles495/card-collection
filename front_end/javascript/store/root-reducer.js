import reduceReducers from 'reduce-reducers'
import { Map, Record } from 'immutable'

import { ApplicationReducer } from '../components/application'
import { RedGreenToggleReducer } from '../components/red-green-toggle'

const INIT_STATE = Map({'root-reduer-test': 'test-value'})

//@TODO REPLACE WITH REAL COMPONENT REDUCERS
let MODULE_ONE_REDUCER = (state, action) => {
  if (action) {
    switch (action.type) {
      case 'component-one.set-some-property':
        return state.setIn(['module-one', 'sub-key'], action.payload)
      default:
        console.log('secondary reducer - default')
        return state
    }
  }
  return state
}

export const rootReducer = reduceReducers(ApplicationReducer
                                        , RedGreenToggleReducer
                                        , INIT_STATE)