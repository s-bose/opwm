<template>
  <!-- <div class="py-16">
    <Switch
      v-model="enabled"
      :class="enabled ? 'bg-red-900' : 'bg-red-700'"
      class="
        relative
        inline-flex
        items-center
        h-6
        rounded-full
        w-11
        transition-colors
        ease-in-out
        duration-200
        focus:outline-none
        focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75
      "
    >
      <span class="sr-only">Enable notifications</span>
      <span
        :class="enabled ? 'translate-x-6' : 'translate-x-1'"
        class="inline-block w-4 h-4 transform bg-white rounded-full ring-0 transition ease-in-out duration-200"
        s
      />
    </Switch>
  </div> -->

  <!-- <div class="container">
    <button class="bg-red-700 text-white h-12 w-12" @click="showPop = !showPop">click me</button>
    <delete-modal v-model:showDelModal="showPop" site="Google" @DeletePass="deletePass" /> -->
  <!-- <password-modal :isEditorMode="false" v-model:showModal="showPop" @newPassword="showPassObj" /> -->

  <!-- <ModalGeneric :modelValue="showPop" @update:modelValue="showPop = $event" /> -->
  <!-- </div> -->
  <login-component :isLogin="true" />
</template>

<script>
// import { ref } from "vue";
// import { Switch } from "@headlessui/vue";
// import DeleteModal from "../components/DeleteModalComponent.vue";
import LoginComponent from "@/components/LoginComponent.vue";
export default {
  name: "Test",
  components: { LoginComponent },
  data() {
    return {
      showPop: false,
    };
  },

  updated() {
    // console.log(this.showPop);
  },
  // components: { Switch },

  // setup() {
  //   const enabled = ref(true);
  //   return { enabled };
  // },
  methods: {
    showPassObj(e) {
      console.log(e);
    },
  },
};
</script>

<style scoped>
</style>
