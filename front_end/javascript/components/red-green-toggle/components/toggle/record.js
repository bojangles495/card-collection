import { Record } from 'immutable'

// import { RED_GREEN_TOGGLE_CONFIG, DEFAULT_RED_GREEN_TOGGLE_CONFIG } from './store-config'

// export const RedGreenToggleRecord = Record(RED_GREEN_TOGGLE_CONFIG)

const RECORD_CONFIG = 
  { checked: undefined
  }

export const createRedGreenToggleRecord = (checkedValue) => {
  const config = RECORD_CONFIG
  config['checked'] = checkedValue
  const RedGreenToggleRecord = Record(config)

  return RedGreenToggleRecord()
}