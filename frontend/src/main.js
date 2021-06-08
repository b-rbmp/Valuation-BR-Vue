/* eslint-disable import/no-extraneous-dependencies */
import '@babel/polyfill';
import 'mutationobserver-shim';
import Vue from 'vue';
import Vuelidate from 'vuelidate';
import './plugins/bootstrap-vue';
import VueGtag from 'vue-gtag';

import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;
Vue.use(Vuelidate);

Vue.use(VueGtag, {
  config: { id: 'G-ELLW2HKME8' },
}, router);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
