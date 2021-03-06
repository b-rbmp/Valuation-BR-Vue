<template>
  <div class="ativo">
    <ativo-content/>
  </div>
</template>

<script>
// @ is an alias to /src
import AtivoContent from '@/components/AtivoContent.vue';

export default {
  name: 'Ativo',
  components: {
    AtivoContent,
  },
};
</script>
