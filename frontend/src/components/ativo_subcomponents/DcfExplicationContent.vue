<template>
  <div class="dcf-exp-content mt-4 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-dcf variant="dark">
            Cálculos
          </b-button>
        </b-card-header>
        <b-collapse id="accordion-dcf" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              DCF (Discounted Cash Flow) é o método de valuation que precifica um investimento
              baseado nos fluxos de caixas projetados para o futuro que este investimento vai gerar.
            </b-card-text>
            <b-card-text>
              Neste site, utiliza-se o lucro por ação como um proxy para o fluxo de caixa, para fins
              de simplificação. Essa abordagem obviamente distorce os resultados do método de fluxo
              de caixa descontado original, funcionando como um "lucro descontado"
            </b-card-text>
            <b-card-text>
              Seja g o crescimento e r a taxa de desconto, o lucro por ação projetado para o ano t é
              dado por:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/LPA_dcf.svg" />
            </b-card-text>
            <b-card-text>
              Trazendo esse lucro por ação no ano t para o presente, devemos aplicar a taxa de
              desconto, que pode ser interpretado como o retorno mínimo aceitável ao ano para um
              determinado investimento. Logo, o NPV (Net Present Value) do lucro por ação no ano t é
              igual à:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/NPV_dcf.svg" />
            </b-card-text>
            <b-card-text>
              Portanto, o cálculo do valor justo segundo o modelo DCF-LPA é feito trazendo os lucros
              por ação projetados para os anos subsequentes para o momento atual (NPV's) e somando
              estes com o NPV para os lucros na perpetuidade, no estágio de crescimento terminal:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/Precojusto_dcf.svg" />
            </b-card-text>
            <b-card-text>
              Sendo que o lucro por ação terminal e o NPV terminal podem ser calculados como:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/LPAterminal_dcf.svg" />
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/NPVterminal_dcf.svg" />
            </b-card-text>
            <b-card-text>
              Podemos ver, nos gráficos a seguir, o LPA e o NPV anual utilizados no cálculo
            </b-card-text>
            <div id="dcf-eps-plot"></div>
            <div id="dcf-npv-plot"></div>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js';

export default {
  name: 'DcfExplicationContent',
  props: {
    eps: Array,
    npv: Array,
    terminal_eps: Number,
    terminal_npv: Number,
    n_anos_total: Number,
  },
  mounted() {
    const epsArray = this.eps.slice(1);
    const npvArray = this.npv.slice(1);
    epsArray.push(this.terminal_eps);
    npvArray.push(this.terminal_npv);
    const epsArrayFormatado = epsArray.map((x) => parseFloat(x.toFixed(2)));
    const npvArrayFormatado = npvArray.map((x) => parseFloat(x.toFixed(2)));

    const anosArrayInt = Array.from({ length: this.n_anos_total - 1 }, (_, index) => index + 1);
    const anosArray = anosArrayInt.map((x) => x.toString());
    anosArray.push('Terminal');

    const trace1 = {
      x: anosArray,
      y: epsArrayFormatado,
      name: 'EPS',
      marker: { color: 'rgb(55, 83, 109)' },
      type: 'bar',
      hovertemplate: 'R$ %{y:.2f}',
    };

    const trace2 = {
      x: anosArray,
      y: npvArrayFormatado,
      name: 'NPV',
      marker: { color: 'rgb(26, 118, 255)' },
      type: 'bar',
      hovertemplate: 'R$ %{y:.2f}',
    };

    const data1 = [trace1];
    const data2 = [trace2];

    const layout1 = {
      title: 'EPS ano à ano',
      xaxis: {
        title: 'Ano',
        tickfont: {
          size: 14,
          color: 'rgb(107, 107, 107)',
        },
        type: 'category',
      },
      yaxis: {
        title: 'R$',
        titlefont: {
          size: 16,
          color: 'rgb(107, 107, 107)',
        },
        tickfont: {
          size: 14,
          color: 'rgb(107, 107, 107)',
        },
      },
      legend: {
        x: 0,
        y: 1.0,
        bgcolor: 'rgba(255, 255, 255, 0)',
        bordercolor: 'rgba(255, 255, 255, 0)',
      },
      bargap: 0.15,
    };
    const layout2 = {};
    Object.assign(layout2, layout1);
    layout2.title = 'NPV ano a ano';

    Plotly.plot('dcf-eps-plot', data1, layout1, { displayModeBar: false, responsive: true });
    Plotly.plot('dcf-npv-plot', data2, layout2, { displayModeBar: false, responsive: true });
  },
};
</script>

<style scoped>
.dcf-exp-content {
  min-width: 50%;
}
</style>
