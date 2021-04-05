import { useState, useEffect } from 'react';
import { getPlayers } from '../requests/player';

export default () => {
  const [players, setPlayers] = useState();

  useEffect(() => {
    getPlayers().then(setPlayers);
  }, []);

  return {
    players
  };
};
