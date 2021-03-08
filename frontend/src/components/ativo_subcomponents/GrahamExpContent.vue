<template>
  <div class="graham-exp-content mt-4 col-lg-8 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-graham variant="info">Cálculos</b-button>
        </b-card-header>
        <b-collapse id="accordion-graham" visible accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              @TODO
            </b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GrahamExpContent',
  props: {
    preco_justo: Number,
    lpa: Number,
    vpa: Number,
  },
};
</script>

<style scoped>
.graham-exp-content {
  min-width: 50%;
}
</style>
