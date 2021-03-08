<template>
  <div class="erro-content">
    <b-container>
      <b-row class="justify-content-center">
        <b-col class="display-4 text-center">
          <b-alert variant="danger" show>
            Ativo não encontrado
          </b-alert>
        </b-col>
      </b-row>
      <br />
      <b-row class="justify-content-center">
        <div class="col-12 col-lg-7 text-center mt-2 mb-5">
          <div class="text-wrap lead">
            <span>
              Apenas ações que relataram lucro líquido positivo nos últimos 12 meses estão
              disponíveis neste site.
            </span>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'ErroContent',
};
</script>

<style scoped></style>
