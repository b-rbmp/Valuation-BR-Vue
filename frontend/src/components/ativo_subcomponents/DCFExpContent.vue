<template>
  <div class="dcf-exp-content mt-4 col-lg-8 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-psbe variant="dark">
            Cálculos
          </b-button>
        </b-card-header>
        <b-collapse id="accordion-dcf" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              DCF (Discounted Cash Flow) é o método de valuation que precifica um
                        investimento baseado nos fluxos de caixas projetados para o futuro que este
                        investimento vai gerar.
            </b-card-text>
            <b-card-text>
              Existem diversos modelos de DCF, sendo o método mais utilizado pelos
                        analistas para realizar o valuation de empresas. Neste site, por motivos de
                        simplificação, limita-se o DCF ao modelo de 2 estágios (1 estágio "atual" +
                        1 estágio terminal), e utiliza-se o lucro líquido como um proxy do fluxo de
                        caixa livre gerado pela empresa, apesar de esta abordagem distorcer os
                        resultados.
            </b-card-text>
            <b-card-text>
              Fórmula: @TODO
            </b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DCFExpContent',
  props: {
    lpa: Number,
    vpa: Number,
  },
};
</script>

<style scoped>
.dcf-exp-content {
  min-width: 50%;
}
</style>
