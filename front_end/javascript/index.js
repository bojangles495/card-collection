try {
  delete window.fetch
} catch (e) {
  window.fetch = undefined
}

import "@babel/polyfill"
require('./fetch')

import { Map } from 'immutable'
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { applyMiddleware, compose, createStore } from 'redux'
import { createLogger } from 'redux-logger'
import ReduxThunk from 'redux-thunk'
import reduceReducers from 'reduce-reducers'

import { ApplicationContainer } from './components/ApplicationContainer'

// console.log('change to the file')

const reducer = (state, action) => state

const preloadedState = Map()
const middleware = [ ReduxThunk ]
if (process.env.DEBUG) {
  const logger = createLogger({ stateTransformer: state => state.toJS() })
  middleware.unshift(logger)
}
const composeEnhancers = 'development' !== process.env.NODE_ENV || 'object' !== typeof window || !window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
  ? compose
  : window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
const enhancer = composeEnhancers(applyMiddleware(...middleware))
const store = createStore(reducer, preloadedState, enhancer)

ReactDOM.render
  ( <Provider store={store}>
      <ApplicationContainer />
    </Provider>
  , document.getElementById('root')
  )
