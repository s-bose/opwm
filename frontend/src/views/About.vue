<template>
  <toast v-model:showToast="displayToast" />

  <button class="bg-black text-white h-12 w-12" @click.prevent="toastHandler">Click me</button>
</template>

<script>
import Toast from "../components/ToastComponent.vue";
export default {
  components: { Toast },
  name: "About",
  data() {
    return {
      displayToast: false,
    };
  },

  methods: {
    toastHandler() {
      this.displayToast = !this.displayToast;
      setTimeout(() => {
        this.displayToast = false;
      }, 1000);
    },
  },
};
</script>

<style>
.fade-pop-enter-active,
.fade-pop-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-pop-enter-from,
.fade-pop-leave-to {
  opacity: 0;
}
</style>