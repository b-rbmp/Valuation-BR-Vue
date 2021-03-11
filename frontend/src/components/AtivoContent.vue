<template>
  <div class="ativo-content">
    <div id="conditionalShowing" v-if="ativos != null">
      <b-container v-if="existAtivo()">
        <b-row class="justify-content-center">
          <b-col class="display-4 text-center pt-3">
            Valuation de <b-badge pill variant="dark"> {{ $route.params.ativo }} </b-badge>
          </b-col>
        </b-row>
        <br /><br />
        <b-card no-body>
          <b-tabs pills card content-class="mt-3" align="center" v-model="tabIndex">
            <b-tab title="Graham" :title-link-class="linkClass(0)" active>
              <b-container>
                <b-row class="justify-content-center">
                  <span class="display-4 method-title text-center">Método de Graham</span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content :preco_justo="1.0" :cotacao_atual="1.53" :upside="51.2" />
                </b-row>
                <b-row class="justify-content-center">
                  <graham-exp-content :lpa="1.4" :vpa="1" />
                </b-row>
                <b-row class="justify-content-center">
                  <grafico-content
                    :precoJusto="100"
                    :graphData="1"
                    :stockName="$route.params.ativo"
                  />
                </b-row>
              </b-container>
            </b-tab>
            <b-tab title="DCF(LPA)" :title-link-class="linkClass(1)">
              <b-container>
                <b-row class="justify-content-center">
                  <span class="display-4 method-title text-center">
                    Método de Fluxo de Caixa Descontado com LPA (DCF-LPA)
                  </span>
                </b-row>
              </b-container>
            </b-tab>
            <b-tab title="Lynch" :title-link-class="linkClass(2)">
              <b-container>
                <b-row class="justify-content-center">
                  <span class="display-4 method-title text-center">
                    Método de Lynch (Valor)
                  </span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content :preco_justo="1.0" :cotacao_atual="1.53" :upside="-51.2" />
                </b-row>
                <b-row class="justify-content-center">
                  <lynch-exp-content
                    :roe="59.1"
                    :preco_lucro="14"
                    :payout="12.4"
                    :dividend_yield="4"
                  />
                </b-row>
              </b-container>
            </b-tab>
            <b-tab title="PSBe" :title-link-class="linkClass(3)">
              <b-container>
                <b-row class="justify-content-center">
                  <span class="display-4 method-title text-center">
                    Método PSBe (Valor)
                  </span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content :preco_justo="1.0" :cotacao_atual="1.53" :upside="-51.2" />
                </b-row>
                <b-row class="justify-content-center">
                  <psbe-exp-content
                    :patr_liquido="3000.12"
                    :receita_liquida="1412.1"
                    :rno="133.1"
                    :lucro_liquido="1234.1"
                    :n_acoes="95103131"
                    :constante="5.5"
                  />
                </b-row>
              </b-container>
            </b-tab>
          </b-tabs>
        </b-card>
      </b-container>
      <erro-content v-else />
    </div>
    <div v-else>
      <b-row class="justify-content-center">
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
import ResultsContent from './ativo_subcomponents/ResultsContent.vue';
import GrahamExpContent from './ativo_subcomponents/GrahamExpContent.vue';
import LynchExpContent from './ativo_subcomponents/LynchExpContent.vue';
import PsbeExpContent from './ativo_subcomponents/PsbeExpContent.vue';
import GraficoContent from './ativo_subcomponents/GraficoContent.vue';

export default {
  name: 'AtivoContent',
  data() {
    return {
      ativos: null,
      tabIndex: 0,
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
    linkClass(idx) {
      if (this.tabIndex === idx) {
        return ['bg-dark', 'text-white'];
      }
      return ['text-dark', 'nav-effect'];
    },
  },
  beforeMount() {
    this.$store.dispatch('loadAtivos').then(() => {
      this.ativos = this.$store.state.ativos.data.ativos;
    });
  },
  components: {
    ErroContent,
    ResultsContent,
    GrahamExpContent,
    LynchExpContent,
    PsbeExpContent,
    GraficoContent,
  },
};
</script>

<style>
/* Not scoped so I can change Bootstrap background-color */
.nav-effect:hover {
  transition: 0.35s;
  background-color: rgba(0, 0, 0, 0.2) !important;
}
</style>

<style scoped>
.method-title {
  font-size: 2rem;
}
</style>
