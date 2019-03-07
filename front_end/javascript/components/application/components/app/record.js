import { Record } from 'immutable'

import { APPLICATION_CONFIG, DEFAULT_APPLICATION_CONFIG } from './store-config'

export const ApplicationRecord = Record(APPLICATION_CONFIG)

export const createDefaultApplicationRecord = () => {
  return ApplicationRecord(DEFAULT_APPLICATION_CONFIG)
}