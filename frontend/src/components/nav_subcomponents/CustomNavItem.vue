<template>
  <div v-b-hover="handleHover">
    <b-nav-item :to="view" class="mr-2 px-2 rounded" :class="isHovered ? 'nav-animation' : ''">
      <span class="font-weight-bold" :class="isHovered ? 'text-animation' : 'text-default'">
        {{ texto }}
      </span>
    </b-nav-item>
  </div>
</template>

<script>
export default {
  name: 'CustomNavItem',
  props: ['view', 'texto'],
  data() {
    return {
      isHovered: false,
    };
  },
  methods: {
    handleHover(hovered) {
      this.isHovered = hovered;
    },
  },
};

</script>

<style scoped>
.nav-animation {
  transition: 0.5s;
  background-color: #ffffff;
}
.text-default {
  color: white;
}
.text-animation {
  transition: 0.75s;
  color: black;
}
</style>
