import { List } from 'immutable'
import urlTemplate from 'url-template'

import { getBaseUrl, getRequestInit } from './common'

const cardsSearchTemplate = urlTemplate.parse('api/cards{?name,types,card_text,match_exact,exclude,match_multi,color*}')

export const getCards = async (name, types, card_text, match_exact, exclude, match_multi, colors) => {
  const baseUrl = getBaseUrl()
  const relativeUrl = cardsSearchTemplate.expand({ name, types, card_text, match_exact, exclude, match_multi, color: [colors.green, colors.red, colors.blue, colors.white, colors.black] })
  const input = new URL(relativeUrl, baseUrl).href
  const headers = new Headers()
  headers.append('Accept', 'application/json')
  const init = getRequestInit('GET', headers)
  const response = await window.fetch(input, init)
  if (!response.ok) {
    throw new Error()
  } else {
    const json = await response.json()
    // const addresses = List(json.map(createAddressRecordFromObject))
    return addresses
  }
}
