import axios from 'axios';

export const getPlayers = () => {
  return axios.get(
    'http://localhost:5000/api/player'
  ).then(
    response => response.data
  );
}
