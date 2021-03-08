<template>
  <div class="graham-content mt-5">
    <b-card-group deck>
      <b-card
        header-bg-variant="dark"
        header="Preço Atual"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text class="lead">R$ {{ cotacao_atual.toFixed(2) }}</b-card-text>
      </b-card>

      <b-card
        header-bg-variant="dark"
        header="Preço Calculado"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text class="lead">R$ {{ preco_justo.toFixed(2) }}</b-card-text>
      </b-card>

      <b-card
        header-bg-variant="dark"
        header="Upside"
        header-text-variant="white"
        text-variant="dark"
        class="card-indicator"
        body-bg-variant="white"
        align="center"
        header-class="card-title"
      >
        <b-card-text :class="upsideClass()"> {{ upside.toFixed(2) }} %</b-card-text>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'GrahamContent',
  props: {
    preco_justo: Number,
    cotacao_atual: Number,
    upside: Number,
  },
  methods: {
    upsideClass() {
      if (this.upside > 0) {
        return ['text-success', 'lead'];
      }
      if (this.upside < 0) {
        return ['text-red', 'lead'];
      }
      return ['text-dark', 'lead'];
    },
  },
};
</script>

<style scoped>
.card-indicator {
  min-width: 10rem;
  max-width: 20rem;
}
.lead {
  font-size: 1.5em;
  font-weight: 300;
}
.card-title {
  font-weight: 500;
}
</style>
