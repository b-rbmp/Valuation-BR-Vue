<template>
  <div class="psbe-exp-content mt-4 col-lg-8 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-psbe variant="dark">
            Cálculos
          </b-button>
        </b-card-header>
        <b-collapse id="accordion-psbe" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              A precificação é feita utilizando apenas 5 entradas: Patrimônio Líquido, Receita
              Líquida, Resultado Não Operacional, Lucro Líquido e Número Total de Ações, além de uma
              constante que representa a correlação entre o lucro líquido das empresas listadas na
              bolsa e o seu valor de mercado
            </b-card-text>
            <b-card-text>
              Preço Justo = @TODO
            </b-card-text>
            <b-card-group deck class="mb-3">
              <b-card header="Patrimônio Líquido" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">R$ {{ patr_liquido.toFixed(2) }} Mi</b-card-text>
              </b-card>
              <b-card header="Receita Líquida" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">R$ {{ receita_liquida.toFixed(2) }} Mi</b-card-text>
              </b-card>
            </b-card-group>
            <b-card-group deck class="mb-3">
              <b-card header="Resultado Não Operacional" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">R$ {{ rno.toFixed(2) }} Mi</b-card-text>
              </b-card>
              <b-card header="Lucro Líquido" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">R$ {{ lucro_liquido.toFixed(2) }} Mi</b-card-text>
              </b-card>
            </b-card-group>
            <b-card-group deck class="mb-3">
              <b-card header="Número Total de Ações" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ n_acoes }} ações</b-card-text>
              </b-card>
              <b-card header="Constante de Correlação" header-tag="header" header-class="mb-0">
                <b-card-text class="lead">{{ constante.toFixed(2) }}</b-card-text>
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
  name: 'PsbeExpContent',
  props: {
    patr_liquido: Number,
    receita_liquida: Number,
    rno: Number,
    lucro_liquido: Number,
    n_acoes: Number,
    constante: Number,
  },
};
</script>

<style scoped>
.psbe-exp-content {
  min-width: 50%;
}
</style>
