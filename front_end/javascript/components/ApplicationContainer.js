import React from 'react'
import { Button } from 'react-bootstrap'
// import { getToken } from '../services/get-token'

export const newAppContainerMethod = async () => {
  // const response = await getToken()
  // console.log(response)
}

let count = 0
export const ApplicationContainer = ({}) => {
  return (
    <div>
      <Button onClick={() => newAppContainerMethod(count)}>Click Me!</Button>
    </div>
  )
}
