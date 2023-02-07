<template>
  <div class="ativo-content-mobile">
    <div id="conditionalShowing" v-if="ativoInfo.status != 'loading' && !errorLoading">
      <b-container fluid v-if="ativoInfo.status == 'success'">
        <b-row class="justify-content-center">
          <b-col class="display-4 ativo-title text-center pt-1">
            Valuation de <b-badge pill variant="dark"> {{ $route.params.ativo }} </b-badge>
          </b-col>
        </b-row>
        <br /><br />
        <b-row class="justify-content-center">
          <div class="col-12 text-center">
            <b-tabs
              pills
              fill
              content-class="mt-3"
              nav-class="navtab-style"
              align="center"
              v-model="tabIndex"
            >
              <b-tab title="Graham" :title-link-class="linkClass(0)" active>
                <b-row class="justify-content-center mt-4">
                  <span class="display-4 method-title text-center">Método de Graham (Valor)</span>
                </b-row>
                <b-row class="justify-content-center">
                  <results-content
                    :preco_justo="ativoInfo.preco_graham"
                    :cotacao_atual="ativoInfo.cotacao"
                    :upside="ativoInfo.upside_graham"
                    class="col-12"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <graham-exp-content
                    :lpa="ativoInfo.stockdata.lpa"
                    :vpa="ativoInfo.stockdata.vpa"
                    class="col-12"
                  />
                </b-row>
                <b-row class="justify-content-center">
                  <grafico-content-mobile
                    :precoJusto="ativoInfo.preco_graham"
                    :graphData="ativoInfo.historico"
                    :stockName="$route.params.ativo"
                    class="col-12"
                    plotId="grahamPlot"
                  />
                </b-row>
              </b-tab>
              <b-tab title="DCF(LPA)" :title-link-class="linkClass(1)">
                <b-row class="justify-content-center mt-4">
                  <span class="display-4 method-title text-center">
                    Método de Fluxo de Caixa Descontado com LPA (DCF-LPA)
                  </span>
                </b-row>
                <b-row class="justify-content-center">
                  <dcf-form-mobile
                    :lpa_real="ativoInfo.stockdata.lpa"
                    :cotacao_atual="ativoInfo.cotacao"
                    :historico="ativoInfo.historico"
                  />
                </b-row>
              </b-tab>
              <b-tab title="Lynch" :title-link-class="linkClass(2)">
                <b-row class="justify-content-center mt-4">
                  <span class="display-4 method-title text-center">
                    Método de Lynch
                  </span>
                </b-row>
                <b-row class="justify-content-center">
                  <span class="text-center method-title lead mr-3 my-2">
                    CRES
                  </span>
                  <b-form-checkbox
                    v-model="switchRoe"
                    class="my-2"
                    name="check-roe"
                    size="lg"
                    checked
                    switch
                  >
                  </b-form-checkbox>
                  <span class="text-center method-title lead my-2 ml-2">
                    ROE
                  </span>
                </b-row>
                <div v-if="switchRoe">
                  <b-row class="justify-content-center">
                    <results-content
                      :preco_justo="ativoInfo.preco_lynch_roe"
                      :cotacao_atual="ativoInfo.cotacao"
                      :upside="ativoInfo.upside_lynch_roe"
                      class="col-12"
                      key="results-roe"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <lynch-exp-content
                      :roe="ativoInfo.stockdata.roe"
                      :preco_lucro="ativoInfo.stockdata.preco_lucro"
                      :payout="ativoInfo.stockdata.payout"
                      :dividend_yield="ativoInfo.stockdata.dividend_yield"
                      class="col-12"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <grafico-content-mobile
                      :precoJusto="ativoInfo.preco_lynch_roe"
                      :graphData="ativoInfo.historico"
                      :stockName="$route.params.ativo"
                      plotId="lynchPlot"
                      class="col-12"
                    />
                  </b-row>
                </div>
                <div v-else>
                  <b-row class="justify-content-center">
                    <results-content
                      :preco_justo="ativoInfo.preco_lynch_cres"
                      :cotacao_atual="ativoInfo.cotacao"
                      :upside="ativoInfo.upside_lynch_cres"
                      class="col-12"
                      key="results-cres"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <lynch-exp-content-cres
                      :crescimento="ativoInfo.stockdata.cres5anos"
                      :preco_lucro="ativoInfo.stockdata.preco_lucro"
                      :dividend_yield="ativoInfo.stockdata.dividend_yield"
                      class="col-12"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <grafico-content-mobile
                      :precoJusto="ativoInfo.preco_lynch_cres"
                      :graphData="ativoInfo.historico"
                      :stockName="$route.params.ativo"
                      plotId="lynchPlotCres"
                      class="col-12"
                    />
                  </b-row>
                </div>
              </b-tab>
              <b-tab title="PSBe" :title-link-class="linkClass(3)">
                <b-row class="justify-content-center mt-4">
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
                      class="col-12"
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
                      :margem_liq="ativoInfo.stockdata.margem_liq"
                      class="col-12"
                    />
                  </b-row>
                  <b-row class="justify-content-center">
                    <grafico-content-mobile
                      :precoJusto="ativoInfo.preco_psbe"
                      :graphData="ativoInfo.historico"
                      :stockName="$route.params.ativo"
                      plotId="psbePlot"
                      class="col-12"
                    />
                  </b-row>
                </div>
              </b-tab>
              <b-row class="mx-1 mt-2">
                <span class="text-center"
                  >Ultima atualização dos dados fundamentalistas:
                  {{ ativoInfo.stockdata.last_updated }}
                </span>
              </b-row>
            </b-tabs>
          </div>
        </b-row>
      </b-container>
      <error-page
        title="Ativo não encontrado"
        msg="Apenas ações que relataram lucro líquido positivo nos últimos 12 meses estão
              disponíveis neste site."
        v-else
      />
    </div>
    <div v-else-if="errorLoading">
      <error-page
        title="Error no Database"
        msg="Ocorreu um erro com os servidores do site. Entre em contato com o administrador"
      />
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
import ErrorPage from './errors/ErrorPage.vue';
import ResultsContent from './ativo_subcomponents/ResultsContent.vue';
import GrahamExpContent from './ativo_subcomponents/GrahamExpContent.vue';
import GraficoContentMobile from './ativo_subcomponents/mobile/GraficoContentMobile.vue';
import LynchExpContent from './ativo_subcomponents/LynchExpContent.vue';
import LynchExpContentCres from './ativo_subcomponents/LynchExpContentCres.vue';
import PsbeExpContent from './ativo_subcomponents/PsbeExpContent.vue';
import DcfFormMobile from './ativo_subcomponents/mobile/DcfFormMobile.vue';

export default {
  name: 'AtivoContentMobile',
  data() {
    return {
      tabIndex: 0,
      ativoInfo: { status: 'loading' },
      switchRoe: true,
      errorLoading: false,
    };
  },
  methods: {
    getAtivo() {
      fetchAtivo(this.$route.params.ativo.toUpperCase())
        .then((response) => {
          this.ativoInfo = response.data;
        })
        .catch(() => {
          this.errorLoading = true;
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
    ErrorPage,
    ResultsContent,
    GrahamExpContent,
    GraficoContentMobile,
    LynchExpContent,
    LynchExpContentCres,
    PsbeExpContent,
    DcfFormMobile,
  },
};
</script>

<style>
/* Not scoped so I can change Bootstrap background-color */
.nav-effect:hover {
  transition: 0.35s;
  background-color: rgba(0, 0, 0, 0.2) !important;
}
.navtab-style {
  background-color: rgba(0, 0, 0, 0.05) !important;
}
</style>

<style scoped>
.method-title {
  font-size: 1.5rem;
}
.ativo-title {
  font-size: 3rem;
}
</style>
