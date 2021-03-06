import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Sobre from '../views/Sobre.vue';
import Ativo from '../views/Ativo.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/sobre',
    name: 'Sobre',
    component: Sobre,
  },
  {
    path: '/ativo/:ativo',
    name: 'Ativo',
    component: Ativo,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
