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
            <div :id="this.plotId"></div>
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
    graphData: Object,
    stockName: String,
    plotId: String,
  },

  mounted() {
    const trace1 = {
      x: Object.values(this.graphData.date),
      y: Object.values(this.graphData.adjclose),
      type: 'scatter',
      mode: 'lines',
      name: `${this.stockName}.Close`,
      line: { color: '#343A4' },
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
          x0: Object.values(this.graphData.date)[0],
          y0: this.precoJusto,
          x1: Object.values(this.graphData.date)[Object.values(this.graphData.date).length - 1],
          y1: this.precoJusto,
          line: {
            color: 'rgb(50, 171, 96)',
            width: 2,
            dash: 'dashdot',
          },
        },
      ],
    };
    const data = [trace1];
    Plotly.plot(this.plotId, data, layout, { displayModeBar: false, responsive: true });
  },
};
</script>

<style scoped>
.grafico-content {
  min-width: 50%;
}
</style>
