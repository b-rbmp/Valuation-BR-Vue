<template>
    <div>
        <b-navbar sticky toggleable="lg" type="dark" variant="dark">
            <b-navbar-brand to="/" class="ml-5 font-weight-bold">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-graph-up" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M0 0h1v15h15v1H0V0zm10 3.5a.5.5 0 0 1 .5-.5h4a.5.5
                    0 0 1 .5.5v4a.5.5 0 0 1-1 0V4.9l-3.613 4.417a.5.5 0 0 1-.74.037L7.06
                    6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609
                    2.61L13.445 4H10.5a.5.5 0 0 1-.5-.5z"
                    />
                </svg>
                Valuation-BR
            </b-navbar-brand>
              <!-- Center aligned nav items -->
              <b-nav-form class="ml-auto">
                  <b-form-input
                    size="md"
                    class="mr-2"
                    placeholder="VIVT3"
                    v-model="ativo"
                    ></b-form-input>
                  <b-button
                    size="md"
                    type="submit"
                    variant="outline-light"
                    @click.prevent="getMeal"
                    >Procurar</b-button>
              </b-nav-form>
              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-navbar-nav>
                    <b-nav-item
                      to="Sobre"
                      class="mr-5"
                      >
                      <span class="text-white font-weight-bold">
                      Sobre
                      </span>
                    </b-nav-item>

                </b-navbar-nav>
              </b-navbar-nav>
              <custom-nav-item title="Sobre" view="Sobre"/>
        </b-navbar>
    </div>
</template>

<script>
import CustomNavItem from './nav_subcomponents/CustomNavItem.vue';

export default {
  name: 'Navigation',
  data() {
    return {
      ativo: '',
    };
  },
  methods: {
    getAtivo() {
      console.log('oi');
      // TODO
    },
  },
  components: {
    CustomNavItem,
  },
};
</script>
