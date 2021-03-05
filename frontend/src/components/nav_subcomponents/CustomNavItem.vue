<template>
    <div class="footer-comp fixed-bottom">
        <b-nav-item
        to="{{ view }}"
        class="mr-5"
        >
            <span class="text-white font-weight-bold">
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
</style>
