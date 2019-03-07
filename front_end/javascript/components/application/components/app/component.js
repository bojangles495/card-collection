import React from 'react'
import { Button, Container } from 'react-bootstrap'

import { SearchFilterComponent } from 'components/search-filter'

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
