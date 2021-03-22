import Vue from 'vue';
import Vuex from 'vuex';

// Imports of Ajax Functions defined in /api
import { fetchAtivos } from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // Single sources of Truth
    ativos: [],
    errored: false,
  },
  mutations: {
    setAtivos(state, payload) {
      state.ativos = payload.ativos;
    },
    setError(state, payload) {
      state.errored = payload.hasError;
    },
  },
  actions: {
    // Asynchronous actions
    loadAtivos(context) {
      return fetchAtivos()
        .then((response) => {
          context.commit('setAtivos', { ativos: response });
          context.commit('setError', { hasError: false });
        })
        .catch((error) => {
          // Error
          console.error(error);
          context.commit('setError', { hasError: true });
        });
    },
  },
  modules: {},
});
