<template>
  <div class="ativo-content">
    <div id="conditionalShowing" v-if="ativoInfo.status != 'loading'">
      <b-container v-if="ativoInfo.status == 'success'">
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
                  <span class="display-4 method-title text-center">Método de Graham (Valor)</span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content
                    :preco_justo="ativoInfo.preco_graham"
                    :cotacao_atual="ativoInfo.cotacao"
                    :upside="ativoInfo.upside_graham"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <graham-exp-content
                    :lpa="ativoInfo.stockdata.lpa"
                    :vpa="ativoInfo.stockdata.vpa"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <grafico-content
                    :precoJusto="ativoInfo.preco_graham"
                    :graphData="ativoInfo.historico"
                    :stockName="$route.params.ativo"
                    plotId="grahamPlot"
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
                    Método de Lynch
                  </span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content
                    :preco_justo="ativoInfo.preco_lynch_roe"
                    :cotacao_atual="ativoInfo.cotacao"
                    :upside="ativoInfo.upside_lynch_roe"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <lynch-exp-content
                    :roe="ativoInfo.stockdata.roe"
                    :preco_lucro="ativoInfo.stockdata.preco_lucro"
                    :payout="ativoInfo.stockdata.payout"
                    :dividend_yield="ativoInfo.stockdata.dividend_yield"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <grafico-content
                    :precoJusto="ativoInfo.preco_lynch_roe"
                    :graphData="ativoInfo.historico"
                    :stockName="$route.params.ativo"
                    plotId="lynchPlot"
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
                <div v-if="ativoInfo.stockdata.isbank">
                  <b-alert show variant="danger" class="mt-5 text-center">
                    Este método não é compatível com empresas do tipo Banco
                  </b-alert>
                </div>
                <div v-else>
                  <b-row class="justify-content-center">
                    <results-content
                      :preco_justo="ativoInfo.preco_psbe"
                      :cotacao_atual="ativoInfo.cotacao"
                      :upside="ativoInfo.upside_psbe"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <psbe-exp-content
                      :patr_liquido="ativoInfo.stockdata.patr_liquido"
                      :receita_liquida="ativoInfo.stockdata.receita_liquida"
                      :rno="0"
                      :lucro_liquido="ativoInfo.stockdata.lucro_liquido"
                      :n_acoes="ativoInfo.stockdata.n_acoes"
                      :constante="5.5"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <grafico-content
                      :precoJusto="ativoInfo.preco_psbe"
                      :graphData="ativoInfo.historico"
                      :stockName="$route.params.ativo"
                      plotId="psbePlot"
                    />
                  </b-row>
                </div>
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
import { fetchAtivo } from '@/api';
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
      ativoInfo: { status: 'loading' },
    };
  },
  methods: {
    getAtivo() {
      fetchAtivo(this.$route.params.ativo.toUpperCase())
        .then((response) => {
          this.ativoInfo = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    linkClass(idx) {
      if (this.tabIndex === idx) {
        return ['bg-dark', 'text-white'];
      }
      return ['text-dark', 'nav-effect'];
    },
  },
  beforeMount() {
    this.getAtivo();
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        this.ativoInfo.status = 'loading';
        this.getAtivo();
      }
    },
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
