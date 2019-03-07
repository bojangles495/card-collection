import { default as NAMESPACE } from './namespace'

export const getRecord = (state, componentId) => {
  if(!state.hasIn([NAMESPACE, componentId])) {
    return false
  } else {
    let record = state.getIn([NAMESPACE, componentId])

    return record
  }
}

export const getCurrentCheckedValue = (state, componentId) => {
  if(!state.hasIn([NAMESPACE, componentId])) {
    return false
  } else {
    let record = state.getIn([NAMESPACE, componentId])

    return record.checked
  }
}