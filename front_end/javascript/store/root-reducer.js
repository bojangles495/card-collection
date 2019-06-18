import reduceReducers from 'reduce-reducers'
import { Map, Record } from 'immutable'

import { RedGreenToggleReducer } from '../components/red-green-toggle'
import { SearchFilterReducer } from '../components/search-filter'
import { ServicesReducer } from '../services'

const INIT_STATE = Map({})

export const rootReducer = reduceReducers(RedGreenToggleReducer
                                        , SearchFilterReducer
                                        , ServicesReducer
                                        , INIT_STATE)