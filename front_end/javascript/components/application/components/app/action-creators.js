import * as APPLICATION_ACTIONS from './actions'
import * as service_endpoints from 'services' 

import { PENDING_STATE } from './store-config'

console.log("PENDING_STATE: ", PENDING_STATE.PENDING)

export const getCards = (...args) => async dispatch => {
  await handlePending(dispatch, async () => {
    const getCardsResponse = await service_endpoints.getCards(...args)
    console.log('getCardsResponse: ', getCardsResponse)
  })
}

const setPending = pending => (
  { type: APPLICATION_ACTIONS.SET_PENDING
  , payload: pending
  }
)

const handleError = (dispatch, e) => {
  if (e.message) {
  	console.log('application : handleError : msg : ', e.message)
  	// @TODO implement toast component
    // dispatch(toastsDispatcher.actionCreators.dispatchAlert(toastsDispatcher.TOAST_ERROR, e.message, 'Error'))
  }
}

const handlePending = async (dispatch, func) => {
  dispatch(setPending(PENDING_STATE.PENDING))
  try {
    await func()
    dispatch(setPending(PENDING_STATE.INITIAL))
  }
  catch (e) {
    handleError(dispatch, e)
    dispatch(setPending(PENDING_STATE.FAILED))
  }
}

export const SERVICES = 
	{ getCards
	}

export const testActionCreator = (consoleValue) => {
	const action = 
		{ type: APPLICATION_ACTIONS.SET_CLICK_HERE
		, payload: consoleValue
		}

	return action
}

export const testActionCreatorTwo = (consoleValue) => {
	const action = 
		{ type: APPLICATION_ACTIONS.SET_CLICK_HERE_TWO
		, payload: consoleValue
		}

	return action
}