import { connect } from 'react-redux'

import { RedGreenToggle } from './component'
import { updateToggle } from './action-creators'
import { getCurrentCheckedValue } from './selectors'

const mapStateToProps = (state, ownProps) => {
  const componentId = !ownProps.componentId ? 'default' : ownProps.componentId
  const checked = getCurrentCheckedValue(state, componentId)

  console.log('mp - componentId: ', componentId)
  console.log('mp - checked: ', checked)
  
  return { componentId, checked }
}

const dispatchProps = 
  { updateToggle
  }

export const RedGreenToggleContainer = connect(mapStateToProps, dispatchProps)(RedGreenToggle)