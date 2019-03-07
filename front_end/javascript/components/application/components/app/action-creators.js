import * as APPLICATION_ACTIONS from './actions'

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