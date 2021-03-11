<template>
  <div class="results-content mt-5 col-lg-9 col-12">
    <b-card-group deck>
      <b-card
        header-bg-variant="dark"
        header="Preço Atual"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator overflow-hidden text-nowrap"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text class="lead card-text">R$ {{ cotacao_atual.toFixed(2) }}</b-card-text>
      </b-card>

      <b-card
        header-bg-variant="dark"
        header="Preço Calculado"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator overflow-hidden text-nowrap"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text class="lead card-text">R$ {{ preco_justo.toFixed(2) }}</b-card-text>
      </b-card>

      <b-card
        header-bg-variant="dark"
        header="Upside"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator overflow-hidden text-nowrap"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text class="card-text lead"
          ><span :class="upsideClass()" :data-icon="upsideIcon()" data-inline="false"> </span>
          {{ upside.toFixed(2) }} %</b-card-text
        >
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'ResultsContent',
  props: {
    preco_justo: Number,
    cotacao_atual: Number,
    upside: Number,
  },
  methods: {
    upsideIcon() {
      if (this.upside > 0) {
        return 'ic:baseline-keyboard-arrow-up';
      }
      if (this.upside < 0) {
        return 'ic:baseline-keyboard-arrow-down';
      }
      return 'ic:baseline-equals';
    },
    upsideClass() {
      if (this.upside > 0) {
        return ['text-success', 'iconify', 'card-icon'];
      }
      if (this.upside < 0) {
        return ['text-danger', 'iconify', 'card-icon'];
      }
      return ['text-dark', 'iconify', 'card-icon'];
    },
  },
};
</script>

<style scoped>
.card-indicator {
  min-width: 12rem;
  max-width: 20rem;
}
.card-text {
  font-size: 1.5em;
  font-weight: 300;
}
.card-icon {
  font-size: 1.5em;
}
.card-title {
  font-weight: 500;
}
</style>
