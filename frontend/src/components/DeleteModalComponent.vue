<template>
  <transition name="fade-modal">
    <div
      class="
        min-w-screen
        h-screen
        animated
        fadeIn
        faster
        fixed
        left-0
        top-0
        flex
        justify-center
        items-center
        inset-0
        z-50
        outline-none
        focus:outline-none
        bg-no-repeat bg-center bg-cover
      "
      v-if="showDelModal"
      id="modal-wrapper"
    >
      <div class="absolute bg-black opacity-80 inset-0 z-0" @click="emitCloseInternal"></div>
      <div class="w-full max-w-lg p-5 m-5 relative my-auto rounded-xl shadow-lg bg-dark-secondary text-white">
        <!--content-->
        <div class="content">
          <!--body-->

          <div class="p-5 flex-auto justify-center">
            <div class="text-center justify-center mb-12 text-red-700">
              <!-- top icon (deletion) -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="50"
                height="50"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="m-auto p-auto"
              >
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                <line x1="10" y1="11" x2="10" y2="17"></line>
                <line x1="14" y1="11" x2="14" y2="17"></line>
              </svg>
            </div>

            <!-- body -->
            <div class="text-center gap-x-4">
              <p class="font-large text-xl mt-2">Deleting entry for "{{ site }}"</p>

              <p class="font-large text-xl mt-2">Are you sure?</p>
            </div>
          </div>
          <!--footer-->
          <div class="grid md:grid-cols-2 gap-10 mt-12 justify-items-center pb-5">
            <button
              class="text-center border-0 p-3 duration-300 hover:bg-green-900 hover:border-green-500 hover:text-white rounded-full shadow-xl w-2/4"
              @click.prevent="submitDelete"
            >
              Confirm
            </button>
            <button
              class="text-center border-0 p-3 duration-300 hover:bg-red-900 hover:text-white rounded-full w-2/4 shadow-xl"
              @click.prevent="emitCloseInternal"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "DeleteModal",
  components: {},
  props: {
    showDelModal: {
      type: Boolean,
      default: false,
    },
    pid: {
      type: String,
      default: "",
    },
    site: {
      type: String,
      default: "",
    },
    link: {
      type: String,
      default: "",
    },
    username: {
      type: String,
      default: "",
    },
    password: {
      type: String,
      default: "",
    },
  },
  emits: ["update:showDelModal", "deletePassword"],

  data() {
    return {};
  },

  methods: {
    ...mapActions(["deletePassword"]),

    emitCloseInternal() {
      this.$emit("update:showDelModal", !this.showDelModal);
    },

    submitDelete() {
      const delObj = Object.assign({}, this.$props);
      this.deletePassword(delObj["pid"]);
      this.$emit("update:showDelModal", !this.showDelModal);
    },
  },
};
</script>

<style scoped lang="postcss">
.form-input {
  @apply rounded-md
          px-4
          py-3
          mt-3
          focus:outline-none
          bg-gray-100
          w-full
          bg-dark-primary;
}

.error-span {
  @apply flex
        items-center
        font-medium
        tracking-wide
        text-xs
        mt-2
        ml-1;
}

.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
}
</style>