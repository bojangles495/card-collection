import * as jsCookie from 'js-cookie'
import { includes } from 'lodash'

// These three things match Spring Security's CsrfFilter and CookieCsrfTokenRepository.
const CSRF_IGNORE_METHODS = ['GET', 'HEAD', 'TRACE', 'OPTIONS']
const CSRF_HEADER_NAME = 'X-XSRF-TOKEN'

export const CSRF_COOKIE_NAME = 'XSRF-TOKEN'
export const CSRF_COOKIE_NONBROWSER = 'non-browser'

// NOTE in a browser, document will be an object-or-string (probably an object).
// In node-based tests, document will be undefined.
// Some code written by other people also relies on undefined-document to indicate non-browser
//    e.g. node_modules/sinon/lib/sinon/util/core/deep-equal.js:3
export const inBrowser = () => (typeof document !== 'undefined')

export const getRequestInit = (method, headers, body) => {
  if (!includes(CSRF_IGNORE_METHODS, method)) {
    const csrfToken = inBrowser() ? jsCookie.get(CSRF_COOKIE_NAME) : CSRF_COOKIE_NONBROWSER
    if (csrfToken) {
      if (!headers) {
        headers = new Headers()
      }
      headers.append(CSRF_HEADER_NAME, csrfToken)
    }
  }
  const init =
    { method
    , headers
    , body
    , mode: 'cors'
    , credentials: 'include'
    , cache: 'default'
    , redirect: 'follow'
    }
  return init
}

const getServiceEndpoint = () => (
  undefined !== window.ecommerce && undefined !== window.ecommerce.serviceEndpoint
    ? window.ecommerce.serviceEndpoint
    : window.location.href
)

// NOTE global.cpqUrl is used during "npm run test:services" which has no document.
// Even if there is a document, it's better to rely on window.location than document.location.
//
// Internet Explorer 11 does not support global.URL but we are using url-polyfill.
export const getBaseUrl = () => new URL('/', (inBrowser() ? getServiceEndpoint() : global.cpqUrl))
