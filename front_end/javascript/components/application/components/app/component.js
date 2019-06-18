import React from 'react'
import { Button, Container } from 'react-bootstrap'

import { SearchFilterContainer } from 'components/search-filter'

export const Application = ({}) => {
  return (
    <div>
        <Container>
            <div className='row'>
                <div className='col-8'>
                    <SearchFilterContainer />
                </div>
            </div>
        </Container>
    </div>
  )
}
