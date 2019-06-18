import React from 'react'
import classNames from 'classnames'

export const RedGreenToggle = ({componentId
                                , checked
                                , children
                                , updateToggle
                                , disabled
                                , label
                                }) =>  {
  const lableClassnameOptions =
    { 'enabled': !disabled
    , 'disabled': disabled
    }
  const labelClassname = classNames('toggle-checkbox-overlay', lableClassnameOptions)
  const toggleId = `red-green-toggle-${componentId}`

  return (
    <div className='red-green-toggle-container'>
      <div className='toggle-label'>
      { children }
      </div>
      <div className='toggle-checkbox-block'>
        <div className='toggle-checkbox-container'>
          <input 
            id={toggleId}
            type="checkbox" 
            checked={checked}
            onClick={(event) => updateToggle(componentId)}
            onChange={() => {}} 
            className='toggle-checkbox'
            disabled={disabled}
          />
          <label className={labelClassname} htmlFor={toggleId} />
        </div>
      </div>
    </div>
  )
}
