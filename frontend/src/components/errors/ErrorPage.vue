<template>
  <div class="error-alert">
    <b-container>
      <b-row class="justify-content-center">
        <b-col class="display-4 text-center">
          <b-alert variant="danger" show>
            {{ title }}
          </b-alert>
        </b-col>
      </b-row>
      <br />
      <b-row class="justify-content-center">
        <div class="col-12 col-lg-9 text-center mt-2 mb-5">
          <div class="text-wrap lead">
            <span>
              {{ msg }}
            </span>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'ErrorBackend',
  props: {
    title: String,
    msg: String,
  },
};
</script>

<style scoped></style>
