const handleError = (dispatch, e) => {
  if (e.message) {
    console.log('application : handleError : msg : ', e.message)
    // @TODO implement toast component
    // dispatch(toastsDispatcher.actionCreators.dispatchAlert(toastsDispatcher.TOAST_ERROR, e.message, 'Error'))
  }
}