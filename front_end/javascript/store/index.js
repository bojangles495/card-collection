import { Record } from 'immutable'

import { APPLICATION_NAMESPACE
        , createDefaultApplicationState } from '../components/application'

//@TODO REPLACE WITH REAL COMPONENTS
const MODULE_ONE_NAMESPACE = 'module-one'
const createDefaultModuleOneState = () => {
    const ModRecord = Record({modOneProperty: undefined})
    return ModRecord({modOneProperty: "property value - mod one"})
}

const MODULE_TWO_NAMESPACE = 'module-two'
const createDefaultModuleTwoState = () => {
    const ModRecord = Record({modTwoProperty: undefined})
    return ModRecord({modTwoProperty: "property value - mod two"})
}

const STORE_CONFIG = 
    { [APPLICATION_NAMESPACE]: undefined
    , [MODULE_ONE_NAMESPACE]: undefined
    , [MODULE_TWO_NAMESPACE]: undefined
    }

const StoreRecord = Record(STORE_CONFIG)

// const DEFAULT_STORE_CONFIG = STORE_CONFIG
// DEFAULT_STORE_CONFIG[APPLICATION_NAMESPACE]: createDefaultApplicationState()
// DEFAULT_STORE_CONFIG[MODULE_ONE_NAMESPACE]: createDefaultModuleOneState()
// DEFAULT_STORE_CONFIG[MODULE_TWO_NAMESPACE]: createDefaultModuleTwoState()

export const STORE = new StoreRecord()