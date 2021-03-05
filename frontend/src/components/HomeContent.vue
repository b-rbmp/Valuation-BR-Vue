<template>
    <div class="home-content">
        <b-container>
            <b-row class="justify-content-md-center">
                <b-col class="display-4 text-center mt-5 pt-3" id='title'>
                    Comparação de Métodos de Valuation
                </b-col>
            </b-row>
            <br><br>
            <b-row class="justify-content-md-center">
                <b-col cols="7" class="text-center mt-4">
                    <span class="lead text-wrap">
                        Compare diferentes métodos de valuation para um determinado ativo,
                        basta pesquisar o ticker acima!
                    </span>
                </b-col>
            </b-row>
            <div class="row justify-content-center">
                <span class="iconify mt-4"
                data-icon="fxemoji:stockchart"
                data-width="300"
                data-height="300"
                data-inline="false"></span>
            </div>
        </b-container>
    </div>
</template>

<script>
export default {
  name: 'HomeContent',
};
</script>

<style scoped>

</style>
