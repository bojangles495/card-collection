import { default as APPLICATION_NAMESPACE } from './namespace'

let PENDING_STATE =
    { IDLE: "idle"
    , PENDING: "pending"
    , COMPLETE: "complete"
    , ERROR: "error"
    }

let createConfig = (pendingState, setClicker, setClickerTwo) => {
    const config =
        { PENDING: pendingState
        , 'set-clicker': setClicker
        , 'set-clicker-two': setClicker
        }
    return config
}

const APPLICATION_CONFIG = createConfig()
const DEFAULT_APPLICATION_CONFIG = createConfig(PENDING_STATE.IDLE)

export { APPLICATION_CONFIG, DEFAULT_APPLICATION_CONFIG }

    