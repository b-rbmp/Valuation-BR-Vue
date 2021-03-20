<template>
  <div class="dcf-form mt-4 col-12">
    <b-row v-if="show" class="justify-content-center">
      <b-form class="col-lg-9" @submit="onSubmit" @reset="onReset">
        <b-card border-variant="light">
          <b-form-group
            label-cols-lg="3"
            label="Dados Iniciais"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Numero de Estágios:"
              label-for="estagios-spin"
              description="Estágios para calcular"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-form-spinbutton
                id="estagios-spin"
                v-model="estagios"
                min="0"
                max="10"
              ></b-form-spinbutton>
            </b-form-group>
            <b-form-group
              label="Lucro Por Ação:"
              label-for="lpa-input"
              description="Valor padrão = LPA atual da empresa"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-input-group prepend="R$">
                <b-form-input
                  id="lpa-input"
                  v-model="form.lpa"
                  step="0.01"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  number
                ></b-form-input>
              </b-input-group>
            </b-form-group>
            <b-form-group
              label="Taxa de Desconto:"
              label-for="txdesconto-input"
              description="Retorno esperado ao ano"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-input-group append="%">
                <b-form-input
                  id="txdesconto-input"
                  v-model="form.tx_desconto"
                  step="0.01"
                  min="0"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  number
                ></b-form-input>
              </b-input-group>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-card border-variant="light">
          <b-form-group
            label-cols-lg="3"
            label="Perpetuidade"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Crescimento:"
              label-for="gperpetuidade-input"
              description="Crescimento na perpetuidade"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-input-group append="%">
                <b-form-input
                  id="gperpetuidade-input"
                  v-model="form.g_perpetuidade"
                  step="0.01"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  number
                ></b-form-input>
              </b-input-group>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-card border-variant="light" v-for="n in estagios" :key="n">
          <b-form-group
            label-cols-lg="3"
            :label="n + '° Estagio'"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Crescimento:"
              :label-for="'gestagio-' + n + '-input'"
              description="Crescimento no estágio"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-input-group append="%">
                <b-form-input
                  :id="'gestagio-' + n + '-input'"
                  step="0.01"
                  v-model="form.vetor_g[n - 1]"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  number
                ></b-form-input>
              </b-input-group>
            </b-form-group>
            <b-form-group
              label="Período:"
              :label-for="'testagio-' + n + '-input'"
              description="Período em anos do estágio"
              label-cols-sm="4"
              label-align-sm="right"
            >
              <b-input-group append="anos">
                <b-form-input
                  :id="'testagio-' + n + '-input'"
                  v-model="form.vetor_anos[n - 1]"
                  min="1"
                  step="1"
                  type="number"
                  lazy-formatter
                  :formatter="formatinteger"
                  number
                ></b-form-input>
                <b-form-invalid-feedback :id="'testagio-' + n + '-input'">
                  Numero de anos acima de 0
                </b-form-invalid-feedback>
              </b-input-group>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-row class="mt-5 justify-content-center">
          <b-button type="submit" class="mx-2" variant="dark">Calcular</b-button>
          <b-button type="reset" class="mx-2" variant="danger">Resetar</b-button>
        </b-row>
      </b-form>
    </b-row>
    <b-row class="justify-content-center" v-else>
      <div class="col-12" v-if="calculated">
        <b-row class="justify-content-center">
          <results-content
            :preco_justo="resultado.valor_justo"
            :cotacao_atual="cotacao_atual"
            :upside="resultado.upside"
            class="col-12 col-lg-9"
          />
        </b-row>
        <b-row class="justify-content-center">
          <dcf-exp-content
            class="col-12 col-lg-9"
            :eps="resultado.eps"
            :npv="resultado.npv"
            :terminal_npv="resultado.terminal_npv"
            :terminal_eps="resultado.terminal_eps"
            :n_anos_total="n_anos_total"
          />
        </b-row>
        <b-row class="justify-content-center">
          <grafico-content
            :precoJusto="resultado.valor_justo"
            :graphData="historico"
            :stockName="$route.params.ativo"
            plotId="dcfPlot"
            class="col-12 col-lg-9"
          />
        </b-row>
      </div>
      <div class="col-12 col-lg-9" v-else>
        <b-row class="justify-content-center">
          <span class="display-4 my-5" style="font-size: 2rem;">Calculando...</span>
        </b-row>
      </div>
    </b-row>
  </div>
</template>

<script>
import ResultsContent from './ResultsContent.vue';
import GraficoContent from './GraficoContent.vue';
import DcfExpContent from './DcfExpContent.vue';

export default {
  name: 'DcfForm',
  components: {
    ResultsContent,
    GraficoContent,
    DcfExpContent,
  },
  data() {
    return {
      estagios: 1,
      calculated: false,
      n_anos_total: 0,
      resultado: {
        valor_justo: 0,
        upside: 0,
        eps: [],
        npv: [],
        terminal_npv: 0,
        terminal_eps: 0,
      },
      form: {
        lpa: parseFloat(this.lpa_real.toFixed(2)),
        vetor_g: [],
        vetor_anos: [],
        g_perpetuidade: 0,
        tx_desconto: 0,
      },
      show: true,
    };
  },
  props: {
    lpa_real: Number,
    cotacao_atual: Number,
    historico: Object,
  },
  methods: {
    formatdigits(value) {
      return parseFloat(value).toFixed(2);
    },
    formatinteger(value) {
      return parseFloat(value).toFixed(0);
    },
    onSubmit(event) {
      event.preventDefault();
      this.calculo_dcf();
      this.show = false;
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.estagios = 1;
      this.form.lpa = parseFloat(this.lpa_real.toFixed(2));
      this.form.vetor_g = [];
      this.form.vetor_anos = [];
      this.form.tx_desconto = 0;
      this.form.g_perpetuidade = 0;
      this.n_anos_total = 0;
      this.calculated = false;
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    calculo_dcf() {
      this.resultado.eps = [];
      this.resultado.npv = [];
      this.resultado.valor_justo = 0;
      this.resultado.terminal_npv = 0;
      this.resultado.terminal_eps = 0;
      this.resultado.upside = 0;
      this.n_anos_total = 0;
      let i;
      let ano = 1;
      this.resultado.eps[0] = this.form.lpa;
      this.resultado.npv[0] = this.form.lpa;
      if (this.estagios > 0) {
        for (i = 1; i <= this.estagios; i += 1) {
          let n;
          for (n = 1; n <= this.form.vetor_anos[i - 1]; n += 1) {
            // eslint-disable-next-line max-len
            this.resultado.eps[ano] = this.resultado.eps[ano - 1] * (1 + this.form.vetor_g[i - 1] / 100);
            // eslint-disable-next-line max-len
            this.resultado.npv[ano] = this.resultado.eps[ano] / (1 + this.form.tx_desconto / 100) ** ano;
            this.resultado.valor_justo += this.resultado.npv[ano];
            ano += 1;
          }
        }
        // eslint-disable-next-line max-len
        this.resultado.terminal_eps = (this.resultado.eps[ano - 1] * (1 + this.form.g_perpetuidade / 100))
          / (this.form.tx_desconto / 100 - this.form.g_perpetuidade / 100);
        // eslint-disable-next-line max-len
        this.resultado.terminal_npv = this.resultado.terminal_eps / (1 + this.form.tx_desconto / 100) ** (ano - 1);
      } else {
        this.resultado.terminal_eps = (this.resultado.eps[0] * (1 + this.form.g_perpetuidade / 100))
          / (this.form.tx_desconto / 100 - this.form.g_perpetuidade / 100);
        // eslint-disable-next-line max-len
        this.resultado.terminal_npv = this.resultado.terminal_eps / (1 + this.form.tx_desconto / 100);
      }
      // eslint-disable-next-line max-len
      this.resultado.valor_justo += this.resultado.terminal_npv;
      this.resultado.upside = (this.resultado.valor_justo / this.cotacao_atual - 1) * 100;
      this.n_anos_total = ano;
      this.calculated = true;
    },
  },
};
</script>

<style scoped></style>
