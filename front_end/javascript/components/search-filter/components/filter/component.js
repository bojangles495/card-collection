import React from 'react'
import { Container, Row, Col, Button } from 'react-bootstrap'

import { RedGreenToggleContainer } from 'components/red-green-toggle'
import { CONSTANTS } from './constants'

export class Filter extends React.Component {
    constructor(props) {
      super(props)

      this.handleInputChange = this.handleInputChange.bind(this)
      this.handleSearchClick = this.handleSearchClick.bind(this)
    }

    isChecked(record, setValue) {
      return record.checked ? setValue : record.checked
    }

    handleSearchClick() {
      const name = this.isChecked(this.props.nameFilterRecord, this.props.inputField)
      const types = this.isChecked(this.props.typesFilterRecord, this.props.inputField)
      const card_text = this.isChecked(this.props.textFilterRecord, this.props.inputField)
      const match_multi = this.isChecked(this.props.multiFilterRecord, 'T')
      const match_exact = this.isChecked(this.props.exactFilterRecord, 'T')
      const exclude = this.isChecked(this.props.excludeFilterRecord, 'T')
      const color = 
        [this.isChecked(this.props.greenManaFilterRecord, 'G')
        , this.isChecked(this.props.redManaFilterRecord, 'R')
        , this.isChecked(this.props.blueManaFilterRecord, 'U')
        , this.isChecked(this.props.whiteManaFilterRecord, 'W')
        , this.isChecked(this.props.blackManaFilterRecord, 'B')
        ]
      const page = 1

      this.props.getCards({name, types, card_text, match_exact, exclude, match_multi, color, page})
    }

    handleInputChange(event) {
      this.props.updateInputField(event.target.value)
    }

    render() {
        return (
            <Container>
                <Row>
                  <Col>
                    <input type='text' style={{width: '100%'}} onChange={this.handleInputChange}/>
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
                      <img src={CONSTANTS.WHITE_MANA_IMAGE} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.GREEN_MANA_FILTER} >
                      <img src={CONSTANTS.GREEN_MANA_IMAGE} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.BLUE_MANA_FILTER} >
                      <img src={CONSTANTS.BLUE_MANA_IMAGE} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.RED_MANA_FILTER} >
                      <img src={CONSTANTS.RED_MANA_IMAGE} style={{width: '30px', height: '30px'}}/>
                    </RedGreenToggleContainer>
                  </Col>
                  <Col>
                    <RedGreenToggleContainer componentId={CONSTANTS.BLACK_MANA_FILTER} >
                      <img src={CONSTANTS.BLACK_MANA_IMAGE} style={{width: '30px', height: '30px'}}/>
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

                <Row>
                  <Col>
                    <div style={{float: "right"}}>
                      <Button onClick={() => this.handleSearchClick()}>Search</Button>
                    </div>
                  </Col>
                </Row>
            </Container>
        )
    }
}
