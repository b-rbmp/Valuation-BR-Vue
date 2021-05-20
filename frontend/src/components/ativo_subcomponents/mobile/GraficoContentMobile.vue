<template>
  <div class="grafico-content mt-3">
    <b-button block variant="dark">
      Gráfico
    </b-button>
    <div :id="this.plotId"></div>
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
      margin: {
        l: 60,
        r: 25,
        b: 50,
        t: 100,
        pad: 4,
      },
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
            {
              step: 'all',
              label: 'tudo',
            },
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
