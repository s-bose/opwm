<template>
  <button
    class="
      fixed
      z-20
      bottom-10
      right-10
      p-0
      w-16
      h-16
      bg-green-600
      rounded-full
      hover:bg-gray-800
      shadow-lg
      active:shadow-lg
      mouse
      shadow
      transition
      ease-in
      duration-200
      focus:outline-none
    "
    @click.prevent="showModal = !showModal"
  >
    <svg
      viewBox="0 0 20 20"
      enable-background="new 0 0 20 20"
      class="w-6 h-6 inline-block"
    >
      <path
        fill="#FFFFFF"
        d="M16,10c0,0.553-0.048,1-0.601,1H11v4.399C11,15.951,10.553,16,10,16c-0.553,0-1-0.049-1-0.601V11H4.601
                                    C4.049,11,4,10.553,4,10c0-0.553,0.049-1,0.601-1H9V4.601C9,4.048,9.447,4,10,4c0.553,0,1,0.048,1,0.601V9h4.399
                                    C15.952,9,16,9.447,16,10z"
      />
    </svg>
  </button>

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
    v-show="showModal"
    id="modal-wrapper"
  >
    <div
      class="absolute bg-black opacity-80 inset-0 z-0"
      @click.prevent="showModal = !showModal"
    ></div>
    <div
      class="
        w-full
        max-w-lg
        p-5
        m-5
        relative
        my-auto
        rounded-xl
        shadow-lg
        bg-white
      "
    >
      <!--content-->
      <div class="content">
        <!--body-->
        <div class="p-5 flex-auto justify-center">
          <div class="text-center justify-center mb-12">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="50"
              height="50"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#000000"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="m-auto p-auto"
            >
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 9.9-1"></path>
            </svg>
          </div>

          <form action="" class="mt-6">
            <div class="my-5 text-sm">
              <label for="site" class="flex text-black text-lg"
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <circle cx="12" cy="12" r="10"></circle>
                </svg>
                Site
              </label>
              <div class="relative w-full"></div>
              <input
                required
                type="text"
                autofocus
                class="form-input"
                v-model="v$.form.site.$model"
                placeholder="ex: google"
              />
            </div>
            <div class="my-5 text-sm">
              <label for="link" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <path
                    d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"
                  ></path>
                  <path
                    d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"
                  ></path>
                </svg>
                Link
                <span class="text-red-500 mx-1">*</span>
              </label>
              <div class="relative w-full"></div>
              <input
                type="text"
                autofocus
                class="form-input"
                v-model="v$.form.link.$model"
                :class="{ 'border-red-500': v$.form.link.$error }"
                placeholder="www.example.com"
              />
              <span
                class="error-span text-red-500"
                v-for="error in v$.form.link.$errors"
                :key="error"
              >
                {{ error.$message }}
              </span>
            </div>

            <div class="my-5 text-sm">
              <label for="username" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                Username
                <span class="text-red-500 mx-1">*</span>
              </label>
              <div class="relative w-full"></div>
              <input
                type="text"
                autofocus
                class="form-input"
                v-model="v$.form.username.$model"
                :class="{ 'border-red-500': v$.form.username.$error }"
                placeholder="john_doe"
              />
              <span
                class="error-span text-red-500"
                v-for="error in v$.form.username.$errors"
                :key="error"
              >
                {{ error.$message }}
              </span>
            </div>
            <div class="my-5 text-sm">
              <label for="password" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <rect
                    x="3"
                    y="11"
                    width="18"
                    height="11"
                    rx="2"
                    ry="2"
                  ></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
                Password
                <span class="text-red-500 mx-1">*</span>
              </label>

              <div class="relative w-full">
                <div
                  class="absolute inset-y-0 right-0 flex items-center px-1 py-3"
                >
                  <button
                    class="
                      hover:bg-gray-200
                      rounded
                      px-2
                      py-1
                      mt-12
                      text-sm text-gray-600
                      hover:rounded-md
                      cursor-pointer
                    "
                    type="button"
                    @mouseup="showPass = !showPass"
                    @mousedown="showPass = !showPass"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="#000000"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    >
                      <path
                        d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"
                      ></path>
                      <circle cx="12" cy="12" r="3"></circle>
                    </svg>
                  </button>
                </div>
              </div>

              <input
                :type="[showPass ? 'text' : 'password']"
                class="form-input"
                v-model="v$.form.password.$model"
                :class="{ 'border-red-500': v$.form.password.$error }"
              />
              <span
                class="error-span text-red-500"
                v-for="error in v$.form.password.$errors"
                :key="error"
              >
                {{ error.$message }}
              </span>
            </div>
          </form>
        </div>
        <!--footer-->
        <div class="p-3 mt-2 text-center space-x-4 md:block">
          <button
            class="
              text-center text-black
              border-0
              p-3
              duration-300
              hover:bg-green-500
              hover:text-white
              rounded-full
              w-auto
              shadow-xl
            "
            @click.prevent="submitForm"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="40"
              height="40"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#000000"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required, url } from "@vuelidate/validators";
export default {
  name: "ModalButton",
  components: {},
  emits: ["newPassword"],
  data() {
    return {
      v$: useVuelidate(),
      form: {
        site: "",
        link: "",
        username: "",
        password: "",
      },

      showPass: false,
      showModal: false,
    };
  },
  validations() {
    return {
      form: {
        site: {},
        link: { required, url },
        username: { required },
        password: { required },
      },
    };
  },

  methods: {
    submitForm() {
      if (this.v$.$validate()) {
        if (this.form.site === "") {
          let url = new URL(this.form.link);

          this.form.site = url.hostname
            .replace(/^(?:https?:\/\/)?(?:www\.)?/i, "")
            .split("/")[0]
            .split(".")[0];
        }

        this.$emit("newPassword", { ...this.form });
        this.form = {};

        this.showModal = !this.showModal;
        this.v$.$reset();
      }
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
          border;
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