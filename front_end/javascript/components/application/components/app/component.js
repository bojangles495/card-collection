import React from 'react'
import { Button, Container } from 'react-bootstrap'

import { SearchFilterComponent } from 'components/search-filter'
import { getCards } from '../services/getCards'

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

export const Application = ({testActionCreator, testActionCreatorTwo}) => {
  return (
    <div>
        <Container>
            <div className='row'>
                <div className='col-8'>
                    <SearchFilterComponent />
                </div>
                <div className='col'>
                    <Button onClick={() => testActionCreator(5)}>Click Me!</Button>
                </div>
                <div className='col'>
                    <Button onClick={() => testActionCreatorTwo(16)}>Click Me 2!</Button>
                </div>
            </div>
        </Container>
    </div>
  )
}
