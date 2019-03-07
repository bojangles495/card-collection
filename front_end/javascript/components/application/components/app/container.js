import { connect } from 'react-redux'

import { Application } from './component'
import { testActionCreator, testActionCreatorTwo } from './action-creators'

const mapStateToProps = (state, ownProps) => {
	return {}
}

const dispatchProps = 
	{ testActionCreator
	, testActionCreatorTwo
	}

export const ApplicationContainer = connect(mapStateToProps, dispatchProps)(Application)