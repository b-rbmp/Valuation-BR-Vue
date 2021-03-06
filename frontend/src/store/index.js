import Vue from 'vue';
import Vuex from 'vuex';

// Imports of Ajax Functions defined in /api
import { fetchAtivos } from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // Single sources of Truth
    ativos: [],
  },
  mutations: {
    setAtivos(state, payload) {
      state.ativos = payload.ativos;
    },
  },
  actions: {
    // Asynchronous actions
    loadAtivos(context) {
      return fetchAtivos()
        .then((response) => context.commit('setAtivos', { ativos: response }))
        .catch(() => {
          // Error
          alert('Um erro ocorreu, tente novamente mais tarde'); // @TODO
        });
    },
  },
  modules: {},
});
