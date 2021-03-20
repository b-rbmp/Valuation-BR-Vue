<template>
  <div class="sobre-content">
    <b-container>
      <b-row class="justify-content-center">
        <b-col class="display-4 text-center">
          Sobre
        </b-col>
      </b-row>
      <br />
      <b-row class="justify-content-center">
        <div class="col-12 col-lg-10 text-center mt-2">
          <div class="text-wrap lead">
            <span>
              Este site foi formulado para permitir a comparação de diferentes metodologias de
              valuation para um determinado ativo. Atualmente estão disponíveis as seguintes
              metodologias:
            </span>
            <div class="accordion mt-3">
              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" class="p-1" role="tab">
                  <b-button block v-b-toggle.accordion-1 variant="dark">
                    Formula de Peter Lynch
                  </b-button>
                </b-card-header>
                <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text class="text-left">
                      <p>
                        O preço justo de uma ação calculada pela fórmula de Peter Lynch é a
                        materialização de sua famosa regra: "Uma empresa que possui um índice P/L
                        igual a sua taxa de crescimento está corretamente precificada."
                      </p>
                      <p>
                        Isso significa que para Peter Lynch, basta igualar o múltiplo PEG (Price *
                        Earnings * Growth) a 1 para descobrir o preço justo de uma empresa.
                      </p>
                      <p>
                        Neste site, foram utilizados duas medidas de crescimento diferentes : O
                        crescimento médio da receita líquida em 5 anos e o (1-Payout)*ROE.
                      </p>
                      <p>
                        É claro que esta regra de bolso era utilizada por Peter Lynch para realizar
                        apenas uma análise rápida de cabeça e não deve sob nenhuma hipótese ser
                        utilizada como regra na escolha definitiva de uma ação ou investimento.
                      </p>
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" class="p-1" role="tab">
                  <b-button block v-b-toggle.accordion-2 variant="dark">
                    DCF (Fluxo de Caixa Descontado)
                  </b-button>
                </b-card-header>
                <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text class="text-left">
                      <p>
                        DCF (Discounted Cash Flow) é o método de valuation que precifica um
                        investimento baseado nos fluxos de caixas projetados para o futuro que este
                        investimento vai gerar.
                      </p>
                      <p>
                        É uma análise que tenta trazer para o presente o preço justo de um
                        investimento projetando quanto dinheiro o investidor vai receber ajustando
                        os fluxos de caixa futuros para o presente, utilizando uma taxa de desconto,
                        que representa o retorno anual ao ano esperado para o investidor com o
                        investimento.
                      </p>
                      <p>
                        Existem diversos modelos de DCF, sendo o método mais utilizado pelos
                        analistas para realizar o valuation de empresas. Neste site utiliza-se o
                        lucro líquido como um proxy do fluxo de caixa livre gerado pela empresa,
                        apesar de esta abordagem distorcer os resultados.
                      </p>
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" class="p-1" role="tab">
                  <b-button block v-b-toggle.accordion-3 variant="dark">
                    Fórmula de Benjamin Graham
                  </b-button>
                </b-card-header>
                <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text class="text-left"
                      ><p>
                        A fórmula de Benjamin Graham permite calcular o valor intrínsico de uma
                        ação, através da seguinte fórmula:
                      </p>
                      <p>
                        Preço Justo = Raiz Quadrada (22,5 * Lucro Por Ação * Valor Patrimonial da
                        Ação)
                      </p>
                      <p>
                        Este método não funciona para qualquer empresa, apenas para aquelas que
                        possuem lucros constantes (estado terminal) e portanto esse método de
                        Valuation se encaixa apenas para empresas que se encaixam no famoso "Value
                        Investing" (E sob nenhuma hipotése deve ser utilizada para empresas
                        "Growth", de Crescimento).
                      </p>
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>
              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" class="p-1" role="tab">
                  <b-button block v-b-toggle.accordion-4 variant="dark">
                    PSBe - Preço Sugerido Pelo Balanço
                  </b-button>
                </b-card-header>
                <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text class="text-left">
                      <p>
                        O método PSBe, popularizado no falecido fórum do InfoMoney, busca precificar
                        ações utilizando apenas 5 entradas: Patrimônio Líquido, Receita Líquida,
                        Resultado Não Operacional, Lucro Líquido e Número Total de Ações, além de
                        uma constante que representa a correlação entre o lucro líquido das empresas
                        listadas na bolsa e o seu valor de mercado
                      </p>
                      <p>
                        Esse método se encaixa na categoria de "Value Investing" já que desconsidera
                        o crescimento das empresas em seus calculos
                      </p>
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>
            </div>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'SobreContent',
};
</script>

<style scoped>
p {
  font-size: 1rem;
}
</style>
