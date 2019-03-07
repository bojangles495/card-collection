import React from 'react'
import { Row } from 'react-bootstrap'

import { RedGreenToggleContainer, getCurrentCheckedValue } from 'components/red-green-toggle'

const nameFilter = 'name-filter'
const typesFilter = 'types-filter'
const textFilter = 'text-filter'
const greenManaFilter = 'green-mana-filter'
const blueManaFilter = 'blue-mana-filter'
const redManaFilter = 'red-mana-filter'
const blackManaFilter = 'black-mana-filter'
const whiteManaFilter = 'white-mana-filter'
const exactFilter = 'exact-filter'
const excludeFilter = 'exclude-filter'
const multiFilter = 'multi-filter'

export class Filter extends React.Component {
    constructor(props) {
      super(props)
    }

    render() {
        return (
            <div className='container-fluid' style={{maxWidth: '400px'}}>
                <Row>
                  <div className='col'>
                    <input type='text' style={{width: '100%'}} />
                  </div>
                </Row>
                <Row>
                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={nameFilter} >
                      <span>Name:</span>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={typesFilter} >
                      <span>Types:</span>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={textFilter} >
                      <span>Text:</span>
                    </RedGreenToggleContainer>
                  </div>

                </Row>

                <Row>
                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={whiteManaFilter} >
                      <img src='https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74' style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={greenManaFilter} >
                      <img src='https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74' style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={blueManaFilter} >
                      <img src='https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74' style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={redManaFilter} >
                      <img src='https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74' style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={blackManaFilter} >
                      <img src='https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74' style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </div>
                </Row>

                <Row>
                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={exactFilter} >
                      <span>Exact:</span>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer componentId={excludeFilter} >
                      <span>Exclude:</span>
                    </RedGreenToggleContainer>
                  </div>

                  <div className='col' style={{marginTop: '5px'}}>
                    <RedGreenToggleContainer 
                      componentId={multiFilter} 
                      disabled={this.props.exactFilterRecord.checked || this.props.excludeFilterRecord}
                    >
                      <span>Match Multi:</span>
                    </RedGreenToggleContainer>
                  </div>
                </Row>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
  const nameFilterRecord = getRecord(state, nameFilter)
  const typesFilterRecord = getRecord(state, typesFilter)
  const textFilterRecord = getRecord(state, textFilter)
  const greenManaFilterRecord = getRecord(state, greenManaFilter)
  const blueManaFilterRecord = getRecord(state, blueManaFilter)
  const redManaFilterRecord = getRecord(state, redManaFilter)
  const blackManaFilterRecord = getRecord(state, blackManaFilter)
  const whiteManaFilterRecord = getRecord(state, whiteManaFilter)
  const exactFilterRecord = getRecord(state, exactFilter)
  const excludeFilterRecord = getRecord(state, excludeFilter)
  const multiFilterRecord = getRecord(state, multiFilter)

  const props = 
    { nameFilterRecord
    , typesFilterRecord
    , textFilterRecord
    , greenManaFilterRecord
    , blueManaFilterRecord
    , redManaFilterRecord
    , blackManaFilterRecord
    , whiteManaFilterRecord
    , exactFilterRecord
    , excludeFilterRecord
    , multiFilterRecord
    }

  return props
}