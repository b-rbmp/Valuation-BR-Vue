/* eslint-disable import/prefer-default-export */
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export function fetchAtivos() {
  return axios.get(`${API_URL}/ativos`);
}
