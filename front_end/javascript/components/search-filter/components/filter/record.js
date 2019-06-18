import { Record } from 'immutable'

const RECORD_CONFIG = 
  { 'input-field': undefined
  }

export const createSearchFilterRecord = (inputValue) => {
  const config = RECORD_CONFIG
  config['input-field'] = inputValue
  const SearchFilterRecord = Record(config)

  return SearchFilterRecord()
}