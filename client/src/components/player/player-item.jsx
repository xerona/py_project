import React from 'react';

export default ({player}) => {
  return (
    <tr>
      <td>{player.first_name}</td>
      <td>{player.last_name}</td>
    </tr>
  );
};
