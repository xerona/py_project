import React, { Component } from 'react';
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'

import PlayerList from './player-list';

class PlayerLayout extends Component {
  render() {
    return (
      <Container>
        <Table striped bordered hover>
          <PlayerList />
        </Table>
      </Container>
    );
  }
};

export default PlayerLayout;
