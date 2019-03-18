import { ApplicationContainer } from './container'
import { default as APPLICATION_NAMESPACE } from './namespace'
import { reducer as ApplicationReducer } from './reducer'
import { createDefaultApplicationRecord } from './record'
import { SERVICES } from './action-creators' 

export { ApplicationContainer
        , APPLICATION_NAMESPACE
        , ApplicationReducer
        , createDefaultApplicationRecord
        , SERVICES 
        }