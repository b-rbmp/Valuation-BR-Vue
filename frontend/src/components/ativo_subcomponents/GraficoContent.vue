<template>
  <div class="grafico-content mt-4 col-lg-8 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-grafico variant="dark">
            Gráfico
          </b-button>
        </b-card-header>
        <b-collapse visible id="accordion-grafico" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              @TODO Grafico
            </b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GraficoContent',
  props: {
    precoJusto: Number,
    graphData: Number,
  },
};
</script>

<style scoped>
.grafico-content {
  min-width: 50%;
}
</style>
