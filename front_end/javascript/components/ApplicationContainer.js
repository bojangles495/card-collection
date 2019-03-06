import React from 'react'
import { Button } from 'react-bootstrap'

import { getCards } from '../services/getCards'
// import { getToken } from '../services/get-token'

export const newAppContainerMethod = async () => {
  // const response = await getToken()
  // console.log(response)
  const name = ""
  const types = ""
  const card_text = ""
  const match_multi = "T"
  const match_exact = "F"
  const exclude = "F"
  const colors =
    { green: "G"
    , red: "R"
    , blue: "U"
    , white: "W"
    , black: "B"
    }
  const template = getCards(name, types, card_text, match_exact, exclude, match_multi, colors)
  console.log("template: ", template)
}

let count = 0
export const ApplicationContainer = ({}) => {
  return (
    <div>
      <Button onClick={() => newAppContainerMethod(count)}>Click Me!</Button>
    </div>
  )
}
