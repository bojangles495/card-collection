import { Record } from 'immutable'

const STORE_CONFIG = {}

const StoreRecord = Record(STORE_CONFIG)

export const STORE = new StoreRecord()