import React from 'react'
import { Button, Container } from 'react-bootstrap'

import { SearchFilterContainer } from 'components/search-filter'
import { getCards } from 'services/getCards'

const name = "elf"
const types = "elf"
const card_text = "elf"
const match_multi = "F"
const match_exact = "F"
const exclude = "F"
const colors =
    { green: "G"
    , red: "R"
    , blue: "U"
    , white: "W"
    , black: "B"
    }

const handleGetCards = async (getCards) => {
    const template = await getCards(name, types, card_text, match_exact, exclude, match_multi, colors)
    console.log("template: ", template)
}

export const Application = ({getCards, testActionCreator, testActionCreatorTwo}) => {
  return (
    <div>
        <Container>
            <div className='row'>
                <div className='col-8'>
                    <SearchFilterContainer />
                </div>
                <div className='col'>
                    <Button onClick={() => handleGetCards(getCards)}>Click Me!</Button>
                </div>
                <div className='col'>
                    <Button onClick={() => testActionCreatorTwo(16)}>Click Me 2!</Button>
                </div>
            </div>
        </Container>
    </div>
  )
}
