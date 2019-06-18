import * as SERVICE_CONSTANTS from './constants'

let createConfig = (serviceState) => {
    const config =
        { 'service-state': serviceState
        }
    return config
}

const TEMPLATE_CONFIG = createConfig()
const DEFAULT_CONFIG = createConfig(SERVICE_CONSTANTS.PENDING_STATE.IDLE)

export { TEMPLATE_CONFIG, DEFAULT_CONFIG }