<template>
  <div class="grafico-content mt-4 col-lg-9 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-grafico variant="dark">
            Gráfico
          </b-button>
        </b-card-header>
        <b-collapse visible id="accordion-grafico" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <div id="pricePlot"></div>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js';

export default {
  name: 'GraficoContent',
  props: {
    precoJusto: Number,
    graphData: Number,
    stockName: String,
  },

  mounted() {
    // Quando integrar, tirar essa arrow function do Plotly, e o unpack.
    Plotly.d3.csv(
      'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv',
      (err, linhas) => {
        function unpack(linhasarg, key) {
          return linhasarg.map((linha) => linha[key]);
        }

        const trace1 = {
          x: unpack(linhas, 'Date'),
          y: unpack(linhas, 'AAPL.High'),
          type: 'scatter',
          mode: 'lines',
          name: `${this.stockName}.High`,
          line: { color: '#17BECF' },
          hovertemplate: 'R$ %{y:.2f}',
        };

        const trace2 = {
          x: unpack(linhas, 'Date'),
          y: unpack(linhas, 'AAPL.Low'),
          type: 'scatter',
          mode: 'lines',
          name: `${this.stockName}.Low`,
          line: { color: '#7F7F7F' },
          hovertemplate: 'R$ %{y:.2f}',
        };

        const layout = {
          title: 'Cotação e Preço Calculado',
          xaxis: {
            autorange: true,
            rangeselector: {
              buttons: [
                {
                  count: 1,
                  label: '1m',
                  step: 'month',
                  stepmode: 'backward',
                },
                {
                  count: 6,
                  label: '6m',
                  step: 'month',
                  stepmode: 'backward',
                },
                {
                  count: 1,
                  label: '1a',
                  step: 'year',
                  stepmode: 'backward',
                },
                { step: 'all' },
              ],
            },
            type: 'date',
          },
          yaxis: {
            title: 'Preço (R$)',
            autorange: true,
            type: 'linear',
          },
          legend: { orientation: 'h' },
          shapes: [
            {
              type: 'line',
              x0: unpack(linhas, 'Date')[0],
              y0: this.precoJusto,
              x1: unpack(linhas, 'Date')[linhas.length - 1],
              y1: this.precoJusto,
              line: {
                color: 'rgb(50, 171, 96)',
                width: 2,
                dash: 'dashdot',
              },
            },
          ],
        };
        const data = [trace1, trace2];
        Plotly.plot('pricePlot', data, layout, { displayModeBar: false, responsive: true });
      },
    );
  },
};
</script>

<style scoped>
.grafico-content {
  min-width: 50%;
}
</style>
