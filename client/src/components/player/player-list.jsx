import React from 'react';
import usePlayers from '../../hooks/player';
import PlayerItem from './player-item';

export default () => {
  const {players} = usePlayers();

  return (
    <React.Fragment>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
        </tr>
      </thead>
      <tbody>
      {players && players.map(player => (
        <PlayerItem
          key={`${player.first_name}_${player.last_name}`}
          player={player}
        >
        </PlayerItem>
      ))}
      </tbody>
    </React.Fragment>
  );
};
