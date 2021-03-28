/* eslint-disable import/prefer-default-export */
import axios from 'axios';

export function fetchAtivos() {
  return axios.get(`${process.env.VUE_APP_API_URL}/ativos`);
}

export function fetchAtivo(ativo) {
  return axios.get(`${process.env.VUE_APP_API_URL}/ativo/${ativo}`);
}

export function fetchDCF(ativo) {
  // CRIAR LOGICA DO FORM DO DCF
  return axios.post(`${process.env.VUE_APP_API_URL}/ativo/${ativo}`);
}
