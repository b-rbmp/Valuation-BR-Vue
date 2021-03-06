<template>
  <div class="erro">
    <erro-content/>
  </div>
</template>

<script>
// @ is an alias to /src
import ErroContent from '@/components/ErroContent.vue';

export default {
  name: 'Erro',
  components: {
    ErroContent,
  },
};
</script>
