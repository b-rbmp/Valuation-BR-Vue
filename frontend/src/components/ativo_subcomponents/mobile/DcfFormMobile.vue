<template>
  <div class="mt-4 container-fluid">
    <b-row v-if="show" class="justify-content-center">
      <b-form @submit="onSubmit" @reset="onReset" novalidate>
        <b-card border-variant="light">
          <b-form-group
            label="Dados Iniciais"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Numero de Estágios:"
              label-for="estagios-spin"
              description="Estágios para calcular"
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
            >
              <b-input-group prepend="R$">
                <b-form-input
                  id="lpa-input"
                  v-model="$v.form.lpa.$model"
                  step="0.01"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  :state="!$v.form.lpa.$error"
                  number
                ></b-form-input>
              </b-input-group>
              <div class="error" v-if="!$v.form.lpa.required">Deve ser preenchido</div>
              <div class="error" v-else-if="!$v.form.lpa.decimal">Deve ser número</div>
              <div class="error" v-else-if="!$v.form.lpa.valorPositivo">Deve ser maior que 0</div>
              <div class="error" v-else-if="!$v.form.lpa.maxValue">
                Valor muito grande
              </div>
            </b-form-group>
            <b-form-group
              label="Taxa de Desconto:"
              label-for="txdesconto-input"
              description="Retorno esperado ao ano"
            >
              <b-input-group append="%">
                <b-form-input
                  id="txdesconto-input"
                  v-model="$v.form.tx_desconto.$model"
                  step="0.01"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  :state="!$v.form.tx_desconto.$error"
                  number
                ></b-form-input>
              </b-input-group>
              <div class="error" v-if="!$v.form.tx_desconto.required">Deve ser preenchido</div>
              <div class="error" v-else-if="!$v.form.tx_desconto.decimal">Deve ser número</div>
              <div class="error" v-else-if="!$v.form.tx_desconto.valorPositivo">
                Deve ser maior que 0
              </div>
              <div class="error" v-else-if="!$v.form.tx_desconto.maxValue">
                Valor muito grande
              </div>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-card border-variant="light">
          <b-form-group
            label="Perpetuidade"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Crescimento:"
              label-for="gperpetuidade-input"
              description="Crescimento na perpetuidade"
            >
              <b-input-group append="%">
                <b-form-input
                  id="gperpetuidade-input"
                  v-model="$v.form.g_perpetuidade.$model"
                  step="0.01"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  :state="!$v.form.g_perpetuidade.$error"
                  number
                ></b-form-input>
              </b-input-group>
              <div class="error" v-if="!$v.form.g_perpetuidade.required">Deve ser preenchido</div>
              <div class="error" v-else-if="!$v.form.g_perpetuidade.decimal">Deve ser número</div>
              <div class="error" v-else-if="!$v.form.g_perpetuidade.minValue">
                Valor muito pequeno
              </div>
              <div class="error" v-else-if="!$v.form.g_perpetuidade.maxValue">
                Valor muito grande
              </div>
              <div class="error" v-else-if="!$v.form.g_perpetuidade.smallerThanDiscount">
                Crescimento na perpetuidade deve ser menor que a taxa de desconto
              </div>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-card border-variant="light" v-for="n in estagios" :key="n">
          <b-form-group
            :label="n + '° Estagio'"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <b-form-group
              label="Crescimento:"
              :label-for="'gestagio-' + n + '-input'"
              description="Crescimento no estágio"
            >
              <b-input-group append="%">
                <b-form-input
                  :id="'gestagio-' + n + '-input'"
                  step="0.01"
                  v-model="$v.form.vetor_g.$each[n - 1].g.$model"
                  type="number"
                  lazy-formatter
                  :formatter="formatdigits"
                  :state="!$v.form.vetor_g.$each[n - 1].g.$error"
                  number
                ></b-form-input>
              </b-input-group>
              <div class="error" v-if="!$v.form.vetor_g.$each[n - 1].g.required">
                Deve ser preenchido
              </div>
              <div class="error" v-else-if="!$v.form.vetor_g.$each[n - 1].g.decimal">
                Deve ser número
              </div>
              <div class="error" v-else-if="!$v.form.vetor_g.$each[n - 1].g.minValue">
                Valor muito pequeno
              </div>
              <div class="error" v-else-if="!$v.form.vetor_g.$each[n - 1].g.maxValue">
                Valor muito grande
              </div>
            </b-form-group>
            <b-form-group
              label="Período:"
              :label-for="'testagio-' + n + '-input'"
              description="Período em anos do estágio"
            >
              <b-input-group append="anos">
                <b-form-input
                  :id="'testagio-' + n + '-input'"
                  v-model="$v.form.vetor_anos.$each[n - 1].anos.$model"
                  min="1"
                  step="1"
                  type="number"
                  lazy-formatter
                  :formatter="formatinteger"
                  :state="!$v.form.vetor_anos.$each[n - 1].anos.$error"
                  number
                ></b-form-input>
              </b-input-group>
              <div class="error" v-if="!$v.form.vetor_anos.$each[n - 1].anos.required">
                Deve ser preenchido
              </div>
              <div class="error" v-else-if="!$v.form.vetor_anos.$each[n - 1].anos.integer">
                Deve ser inteiro
              </div>
              <div class="error" v-else-if="!$v.form.vetor_anos.$each[n - 1].anos.valorPositivo">
                Deve ser positivo
              </div>
              <div class="error" v-else-if="!$v.form.vetor_anos.$each[n - 1].anos.maxValue">
                Valor muito grande
              </div>
            </b-form-group>
          </b-form-group>
        </b-card>
        <b-card>
        <b-row class="justify-content-center">
          <b-alert variant="danger" :show="errors">
            Conserte todos os erros do formulário
          </b-alert>
        </b-row>
        <b-row class="mt-4 justify-content-center">
          <b-button type="submit" class="mx-2" variant="dark">Calcular</b-button>
          <b-button type="reset" class="mx-2" variant="warning">Limpar</b-button>
        </b-row>
        </b-card>
      </b-form>
    </b-row>
    <b-row class="justify-content-center" v-else>
      <div class="col-12" v-if="calculated">
        <b-row class="justify-content-center">
          <results-content
            :preco_justo="resultado.valor_justo"
            :cotacao_atual="cotacao_atual"
            :upside="resultado.upside"
            class="col-12"
          />
        </b-row>
        <b-row class="justify-content-center">
          <dcf-explication-content
            class="col-12"
            :eps="resultado.eps"
            :npv="resultado.npv"
            :terminal_npv="resultado.terminal_npv"
            :terminal_eps="resultado.terminal_eps"
            :n_anos_total="n_anos_total"
          />
        </b-row>
        <b-row class="justify-content-center">
          <grafico-content-mobile
            :precoJusto="resultado.valor_justo"
            :graphData="historico"
            :stockName="$route.params.ativo"
            plotId="dcfPlot"
            class="col-12"
          />
        </b-row>
        <b-row class="justify-content-center">
          <div class="col-12 mt-4">
            <b-button v-on:click="onReset" block variant="warning">
              Recalcular
            </b-button>
          </div>
        </b-row>
      </div>
      <div class="col-12" v-else>
        <b-row class="justify-content-center">
          <span class="display-4 my-5" style="font-size: 2rem;">Calculando...</span>
        </b-row>
      </div>
    </b-row>
  </div>
</template>

<script>
import { required, decimal, integer } from 'vuelidate/lib/validators';
import ResultsContent from '../ResultsContent.vue';
import GraficoContentMobile from './GraficoContentMobile.vue';
import DcfExplicationContent from '../DcfExplicationContent.vue';

export default {
  name: 'DcfForm',
  components: {
    ResultsContent,
    GraficoContentMobile,
    DcfExplicationContent,
  },
  data() {
    return {
      errors: false,
      calculated: false,
      show: true,
      n_anos_total: 0,
      estagios: 1,
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
        vetor_g: [
          {
            g: 0,
          },
        ],
        vetor_anos: [
          {
            anos: 0,
          },
        ],
        g_perpetuidade: 0,
        tx_desconto: 0,
      },
    };
  },
  props: {
    lpa_real: Number,
    cotacao_atual: Number,
    historico: Object,
  },
  beforeUpdate() {
    if (this.estagios > this.form.vetor_g.length) {
      this.form.vetor_g.push({ g: 0 });
      this.form.vetor_anos.push({ anos: 0 });
    } else if (this.estagios < this.form.vetor_g.length) {
      this.form.vetor_g.pop();
      this.form.vetor_anos.pop();
    }
    this.$v.$touch();
  },
  mounted() {
    // Initialize state for the form validation logic
    this.$v.$touch();
  },
  methods: {
    formatdigits(value) {
      if (value) {
        return parseFloat(parseFloat(value).toFixed(2));
      }
      return 0;
    },
    formatinteger(value) {
      if (value) {
        return parseFloat(parseFloat(value).toFixed(0));
      }
      return 0;
    },
    onSubmit(event) {
      event.preventDefault();
      this.$v.$touch();
      if (this.$v.$invalid) {
        this.errors = true;
      } else {
        this.calculo_dcf();
        this.erros = false;
        this.show = false;
      }
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.estagios = 1;
      this.form.lpa = parseFloat(this.lpa_real.toFixed(2));
      this.form.vetor_g = [
        {
          g: 0,
        },
      ];
      this.form.vetor_anos = [
        {
          anos: 0,
        },
      ];
      this.form.tx_desconto = 0;
      this.form.g_perpetuidade = 0;
      this.n_anos_total = 0;
      this.calculated = false;
      this.errors = false;
      // Reevaluate the state for the form
      this.$v.$touch();
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
          for (n = 1; n <= this.form.vetor_anos[i - 1].anos; n += 1) {
            // eslint-disable-next-line max-len
            this.resultado.eps[ano] = this.resultado.eps[ano - 1] * (1 + this.form.vetor_g[i - 1].g / 100);
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
  validations: {
    form: {
      lpa: {
        required,
        decimal,
        valorPositivo(value) {
          return value > 0;
        },
        maxValue(value) {
          return value < 10000;
        },
      },
      g_perpetuidade: {
        required,
        decimal,
        minValue(value) {
          return value > -1000;
        },
        maxValue(value) {
          return value < 1000;
        },
        smallerThanDiscount(value) {
          return value < this.form.tx_desconto;
        },
      },
      tx_desconto: {
        required,
        decimal,
        valorPositivo(value) {
          return value > 0;
        },
        maxValue(value) {
          return value < 1000;
        },
      },
      vetor_g: {
        $each: {
          g: {
            required,
            decimal,
            minValue(value) {
              return value > -1000;
            },
            maxValue(value) {
              return value < 1000;
            },
          },
        },
      },
      vetor_anos: {
        $each: {
          anos: {
            required,
            integer,
            valorPositivo(value) {
              return value > 0;
            },
            maxValue(value) {
              return value <= 100;
            },
          },
        },
      },
    },
  },
};
</script>

<style scoped>
.error {
  color: rgb(184, 11, 11);
  font-size: 0.8rem;
}
</style>
