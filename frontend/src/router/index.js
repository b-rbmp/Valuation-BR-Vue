import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Sobre from '../views/Sobre.vue';
import Ativo from '../views/Ativo.vue';
import Erro from '../views/Erro.vue';

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
    path: '/ativo',
    name: 'Ativo',
    component: Ativo,
  },
  {
    path: '/erro',
    name: 'Erro',
    component: Erro,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
