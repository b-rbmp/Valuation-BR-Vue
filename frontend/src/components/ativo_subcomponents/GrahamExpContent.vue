<template>
  <div class="graham-exp-content mt-4 col-12">
    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-graham variant="dark">
            Cálculos
          </b-button>
        </b-card-header>
        <b-collapse id="accordion-graham" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>
              A fórmula de Benjamin Graham permite calcular o valor intrínsico de uma ação, através
              da seguinte fórmula:
            </b-card-text>
            <b-card-text class="text-center">
              <img class="img-fluid" src="@/assets/svg/Graham.svg" />
            </b-card-text>
            <b-card-group deck>
              <b-card
                header="LPA (Lucro por Ação)"
                header-tag="header"
                header-class="mb-0"
              >
                <b-card-text class="lead">{{ formatter.format(lpa) }}</b-card-text>
              </b-card>
              <b-card
                header="VPA (Valor patrimonial da Ação)"
                header-tag="header"
                header-class="mb-0"
              >
                <b-card-text class="lead">{{ formatter.format(vpa) }}</b-card-text>
              </b-card>
            </b-card-group>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line import/extensions
import Util from '../util.js';

export default {
  name: 'GrahamExpContent',
  data() {
    return {
      formatter: Util.formatter,
    };
  },
  props: {
    lpa: Number,
    vpa: Number,
  },
};
</script>

<style scoped>
.graham-exp-content {
  min-width: 50%;
}
</style>
