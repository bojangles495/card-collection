import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import { RedGreenToggleContainer } from 'components/red-green-toggle'
import { CONSTANTS } from './constants'

const tempImage = 'https://gamepedia.cursecdn.com/mtgsalvation_gamepedia/8/8e/W.svg?version=d74ba6b898f8815799b1506eb06fdf74'

export class Filter extends React.Component {
    constructor(props) {
      super(props)
    }

    render() {
      console.log('Filter: this.props: ', this.props)
        return (
            <Container>
                <Row>
                  <Col>
                    <input type='text' style={{width: '100%'}} />
                  </Col>
                </Row>
                <Row>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.CARD_NAME_FILTER} >
                      <span>Name:</span>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.CARD_TYPES_FILTER} >
                      <span>Types:</span>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.CARD_TEXT_FILTER} >
                      <span>Text:</span>
                    </RedGreenToggleContainer>
                  </Col>

                </Row>

                <Row>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.WHITE_MANA_FILTER} >
                      <img src={tempImage} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.GREEN_MANA_FILTER} >
                      <img src={tempImage} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.BLUE_MANA_FILTER} >
                      <img src={tempImage} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.RED_MANA_FILTER} >
                      <img src={tempImage} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.BLACK_MANA_FILTER} >
                      <img src={tempImage} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>
                </Row>

                <Row>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.EXACT_FILTER} >
                      <span>Exact:</span>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.EXCLUDE_FILTER} >
                      <span>Exclude:</span>
                    </RedGreenToggleContainer>
                  </Col>

                  <Col>
                    <RedGreenToggleContainer 
                      componentId={CONSTANTS.MATCH_MULTI_FILTER} 
                      disabled={false}
                    >
                      <span>Match Multi:</span>
                    </RedGreenToggleContainer>
                  </Col>
                </Row>
            </Container>
        )
    }
}
