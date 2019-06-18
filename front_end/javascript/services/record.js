import { Record } from 'immutable'

import { TEMPLATE_CONFIG, DEFAULT_CONFIG } from './store-config'

export const ServiceStateRecord = Record(TEMPLATE_CONFIG)

export const createDefaultState = () => {
  return ServiceStateRecord(DEFAULT_CONFIG)
}