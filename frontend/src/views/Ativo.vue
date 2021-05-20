<template>
  <div v-if="!isMobile()" class="ativo">
    <ativo-content />
  </div>
  <div v-else class="ativomobile">
    <ativo-content-mobile />
  </div>
</template>

<script>
// @ is an alias to /src
import AtivoContent from '@/components/AtivoContent.vue';
import AtivoContentMobile from '@/components/AtivoContentMobile.vue';

export default {
  name: 'Ativo',
  methods: {
    isMobile() {
      // eslint-disable-next-line no-restricted-globals
      if (screen.width <= 760) {
        return true;
      }
      return false;
    },
  },
  components: {
    AtivoContent,
    AtivoContentMobile,
  },
};
</script>
