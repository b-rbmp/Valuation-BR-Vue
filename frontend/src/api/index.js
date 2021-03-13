/* eslint-disable import/prefer-default-export */
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export function fetchAtivos() {
  return axios.get(`${API_URL}/ativos`);
}

export function fetchAtivo(ativo) {
  return axios.get(`${API_URL}/ativo/${ativo}`);
}

export function fetchDCF(ativo) {
  // CRIAR LOGICA DO FORM DO DCF
  return axios.post(`${API_URL}/ativo/${ativo}`);
}
