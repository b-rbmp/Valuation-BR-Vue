<template>
  <div class="fixed-top">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand to="/" class="ml-5 font-weight-bold">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          fill="currentColor"
          class="bi bi-graph-up"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M0 0h1v15h15v1H0V0zm10 3.5a.5.5 0 0 1 .5-.5h4a.5.5
                    0 0 1 .5.5v4a.5.5 0 0 1-1 0V4.9l-3.613 4.417a.5.5 0 0 1-.74.037L7.06
                    6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609
                    2.61L13.445 4H10.5a.5.5 0 0 1-.5-.5z"
          />
        </svg>
        Valuation-BR
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <!-- Center aligned nav items -->
        <b-nav-form class="ml-auto my-2 my-lg-0 justify-content-center mr-lg-4">
          <b-form-input
            size="md"
            class="mr-lg-2 col-12 col-lg-7"
            placeholder="VIVT3"
            v-model="ativo"
          ></b-form-input>
          <b-button
            size="md"
            type="submit"
            variant="outline-light"
            class="my-2 my-sm-0 col-12 col-lg-4"
            v-on:click.prevent="searchAtivo"
            >Procurar</b-button
          >
        </b-nav-form>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="text-center ml-lg-auto my-2 my-lg-0 justify-content-center">
          <custom-nav-item texto="Sobre" view="/sobre" />
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import CustomNavItem from './nav_subcomponents/CustomNavItem.vue';

export default {
  name: 'Navigation',
  data() {
    return {
      ativo: '',
    };
  },
  methods: {
    searchAtivo() {
      if (this.ativos.includes(this.ativo.toUpperCase())) {
        this.$router.push({ name: 'Ativo', params: { ativo: this.ativo.toUpperCase() } });
      } else {
        alert('Ativo não encontrado'); // @TODO, fazer com popover
      }
    },
  },
  computed: mapState({
    ativos: (state) => state.ativos.data.ativos,
  }),
  beforeMount() {
    this.$store.dispatch('loadAtivos');
  },
  components: {
    CustomNavItem,
  },
};
</script>
