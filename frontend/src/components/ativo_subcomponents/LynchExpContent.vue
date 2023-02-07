<template>
  <div class="lynch-exp-content mt-4 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-lynch variant="dark">
            Cálculos
          </b-button>
        </b-card-header>
        <b-collapse id="accordion-lynch" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              O preço justo de uma ação calculada pela fórmula de Peter Lynch é a materialização de
              sua famosa regra: "Uma empresa que possui um índice P/L igual a sua taxa de
              crescimento está corretamente precificada.
            </b-card-text>
            <b-card-text>
              Isso significa que para Peter Lynch, basta igualar o múltiplo PEG (Price * Earnings *
              Growth) a 1 para descobrir o preço justo de uma empresa.
            </b-card-text>
            <b-card-text>
              Além do crescimento, que nesta opção é calculado usando o ROE e o Payout da empresa ,
              foi levado também em consideração o dividend yield, sendo então a fórmula final:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/Lynch_ROE_PEG.svg" />
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/Lynch.svg" />
            </b-card-text>
            <b-card-group deck class="mb-3">
              <b-card header="Preço/Lucro" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ preco_lucro.toFixed(2) }}</b-card-text>
              </b-card>
              <b-card header="ROE" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ (roe * 100).toFixed(2) }} %</b-card-text>
              </b-card>
            </b-card-group>
            <b-card-group deck class="mb-3">
              <b-card header="Payout" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ (payout * 100).toFixed(2) }} %</b-card-text>
              </b-card>
              <b-card header="Dividend Yield" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ (dividend_yield * 100).toFixed(2) }} %</b-card-text>
              </b-card>
            </b-card-group>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LynchExpContent',
  props: {
    preco_lucro: Number,
    roe: Number,
    payout: Number,
    dividend_yield: Number,
  },
};
</script>

<style scoped>
.lynch-exp-content {
  min-width: 50%;
}
</style>
