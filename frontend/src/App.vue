<template>
  <div id="app">
    <navigation/>
    <router-view/>
    <footer-comp/>
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue';
import FooterComp from './components/FooterComp.vue';

export default {
  name: 'App',
  components: {
    Navigation,
    FooterComp,
  },
};
</script>
