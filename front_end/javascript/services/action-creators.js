import * as SERVICE_CONSTANTS from './constants'
import * as ACTIONS from './actions'
import * as Cards from './Cards'

const setServiceState = serviceState => {
  return { type: ACTIONS.SET_SERVICE_STATE
          , payload: serviceState
          }
}

const handleError = (dispatch, e) => {
  if (e.message) {
    console.log('application : handleError : msg : ', e.message)
    // @TODO implement toast component
    // dispatch(toastsDispatcher.actionCreators.dispatchAlert(toastsDispatcher.TOAST_ERROR, e.message, 'Error'))
  }
}

const handleServiceState = async (dispatch, func, optional) => {
  dispatch(setServiceState(SERVICE_CONSTANTS.PENDING_STATE.PENDING))
  try {
    const result = await func(optional)
    console.log('result: ', result)

    dispatch(setServiceState(SERVICE_CONSTANTS.PENDING_STATE.IDLE))
  }
  catch (e) {
    handleError(dispatch, e)
    dispatch(setServiceState(SERVICE_CONSTANTS.PENDING_STATE.ERROR))
  }
}



export const getCards = (...args) => async dispatch => {
  await handleServiceState(dispatch, Cards.get, {...args[0]})
}