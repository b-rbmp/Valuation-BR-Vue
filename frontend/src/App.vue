<template>
  <div id="app">
    <navigation />
    <div v-if="!$store.state.errored">
      <router-view />
    </div>
    <div v-else>
      <error-page
        title="Erro"
        msg="Houve um erro de comunicação com o servidor e portanto o site está inutilizável. Favor
              retornar mais tarde até que o erro seja consertado"
      />
    </div>
    <footer-comp />
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue';
import FooterComp from './components/FooterComp.vue';
import ErrorPage from './components/errors/ErrorPage.vue';

export default {
  name: 'App',
  components: {
    Navigation,
    FooterComp,
    ErrorPage,
  },
};
</script>

<style>
body {
  background-color: rgba(0, 0, 0, 0.03);
  padding: 6rem 0rem 0rem 0rem;
}
</style>
