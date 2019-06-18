try {
  delete window.fetch
} catch (e) {
  window.fetch = undefined
}

require('@babel/polyfill')
require('./fetch')

const { Map } = require('immutable')
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { applyMiddleware, compose, createStore } from 'redux'
import { createLogger } from 'redux-logger'
import ReduxThunk from 'redux-thunk'

import { STORE } from './store'
import { rootReducer } from './store/root-reducer'
import { Application } from './components/application'

const testMiddleware = ({dispatch, getState}) => {
  return next => action => {
    const currentState = getState()
    console.log('currentState: ', currentState.toJS())
    const updatedState = next(action)
    console.log('updatedState: ', updatedState)
  }
}

const logger = createLogger({ stateTransformer: state => state.toJS() })
const middleware = [ logger, ReduxThunk, testMiddleware ]
const composeEnhancers = 'development' !== process.env.NODE_ENV || 'object' !== typeof window || !window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
  ? compose
  : window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
const enhancer = composeEnhancers(applyMiddleware(...middleware))
const preloadedState = Map({})
const store = createStore(rootReducer, preloadedState, enhancer)

ReactDOM.render
  ( <Provider store={store}>
      <Application />
    </Provider>
  , document.getElementById('root')
  )
