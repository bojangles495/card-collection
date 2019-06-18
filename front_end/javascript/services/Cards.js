import { List } from 'immutable'
import urlTemplate from 'url-template'

import { getBaseUrl, getRequestInit } from './common'

const cardsSearchTemplate = urlTemplate.parse('api/cards{?name,types,card_text,match_exact,exclude,match_multi,page,color*}')
export const get = async (...args) => {
  const searchCriteria = {...args[0]}
  const baseUrl = getBaseUrl()
  const relativeUrl = cardsSearchTemplate.expand(searchCriteria)
  const input = new URL(relativeUrl, baseUrl).href
  const headers = new Headers()
  headers.append('Accept', 'application/json')
  headers.append('Content-Type', 'application/json')
  const init = getRequestInit('GET', headers)
  const response = await window.fetch(input, init)
  const json = await response.json()

  return json
}

const post = () => {
  // @TODO - Implement Cards POST 
}

const put = () => {
  // @TODO - Implement Cards PUT 
}
