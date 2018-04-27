import React, {Component} from "react"
import { Container, Row, Col } from 'reactstrap'

import GameTab from './DashBoard/GameTab'
import NavigationBar from './DashBoard/NavigationBar'
import StatsBar from './DashBoard/StatsBar'

const Dashboard = () => (
  <Container>
    <Row>
      <NavigationBar />
    </Row>
    <Row>
      <GameTab />
    </Row>
    <Row>
      <StatsBar />
    </Row>
  </Container>
)

export default Dashboard