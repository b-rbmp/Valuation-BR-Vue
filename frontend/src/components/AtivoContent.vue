<template>
  <div class="ativo-content">
    <div id="conditionalShowing" v-if="ativos != null">
      <b-container v-if="existAtivo()">
        <b-row class="justify-content-md-center">
          <b-col class="display-4 text-center mt-2 pt-3">
            Valuation de <b-badge pill variant="dark"> {{ $route.params.ativo }} </b-badge>
          </b-col>
        </b-row>
        <br />
      </b-container>
      <erro-content v-else />
    </div>
    <div v-else>
      <b-row class="justify-content-md-center">
        <b-col class="display-4 text-center mt-2 pt-3">
          Carregando...
        </b-col>
      </b-row>
      <br />
    </div>
  </div>
</template>

<script>
import ErroContent from './ativo_subcomponents/ErroContent.vue';

export default {
  name: 'AtivoContent',
  data() {
    return {
      ativos: null,
    };
  },
  methods: {
    existAtivo() {
      if (this.ativos) {
        if (this.ativos.includes(this.$route.params.ativo.toUpperCase())) {
          return true;
        }
        return false;
      }
      return false;
    },
  },
  beforeMount() {
    this.$store.dispatch('loadAtivos').then(() => {
      this.ativos = this.$store.state.ativos.data.ativos;
    });
  },
  components: {
    ErroContent,
  },
};
</script>

<style scoped></style>
