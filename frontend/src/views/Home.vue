<template>
  <div class="home">
    <home-content/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeContent from '@/components/HomeContent.vue';

export default {
  name: 'Home',
  components: {
    HomeContent,
  },
};
</script>
