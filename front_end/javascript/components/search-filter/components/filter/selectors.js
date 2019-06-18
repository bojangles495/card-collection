import NAMESPACE from './namespace'
export const getInputField = (state) => {
  const getInputField = state.getIn([NAMESPACE, 'input-field'])

  return getInputField
}