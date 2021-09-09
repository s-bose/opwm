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
      v-if="showModal"
      id="modal-wrapper"
    >
      <div class="absolute bg-black opacity-80 inset-0 z-0" @click="emitCloseInternal"></div>
      <div class="w-full max-w-lg p-5 m-5 relative my-auto rounded-xl shadow-lg bg-dark-secondary text-white">
        <!--content-->
        <div class="content">
          <!--body-->

          <div class="p-5 flex-auto justify-center">
            <div class="text-center justify-center mb-12" :class="[isEditorMode ? 'text-white' : 'text-green-500']">
              <!-- top icon (creation) -->
              <svg
                v-if="!isEditorMode"
                xmlns="http://www.w3.org/2000/svg"
                width="19"
                height="19"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="m-auto p-auto mb-2"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="16"></line>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
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
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 9.9-1"></path>
              </svg>
            </div>

            <form action="" class="mt-6">
              <div class="my-5 text-sm">
                <label for="site" class="flex text-lg"
                  ><svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="26"
                    height="26"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="mr-2"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                  </svg>
                  Site
                  <span class="text-red-500 mx-1">*</span>
                </label>
                <div class="relative w-full">
                  <div class="absolute inset-y-0 right-0 flex items-center px-1 py-3">
                    <button class="rounded px-2 py-1 mt-11 text-sm hover:rounded-md cursor-pointer" type="button" @click.prevent="autoFillSite">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="26"
                        height="26"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <path d="M2.5 2v6h6M21.5 22v-6h-6" />
                        <path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2" />
                        <title>autofill site</title>
                      </svg>
                    </button>
                  </div>
                </div>
                <input
                  required
                  type="text"
                  autofocus
                  class="form-input"
                  v-model="form.site"
                  placeholder="ex: google"
                  :class="{ 'border border-red-500': v$.form.site.$error }"
                />
                <span class="error-span text-red-500" v-for="error in v$.form.site.$errors" :key="error">
                  {{ error.$message }}
                </span>
              </div>
              <div class="my-5 text-sm">
                <label for="link" class="flex text-lg">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="26"
                    height="26"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="mr-2"
                  >
                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
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
                  :class="{ 'border border-red-500': v$.form.link.$error }"
                  placeholder="www.example.com"
                />
                <span class="error-span text-red-500" v-for="error in v$.form.link.$errors" :key="error">
                  {{ error.$message }}
                </span>
              </div>

              <div class="my-5 text-sm">
                <label for="username" class="flex text-lg">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="26"
                    height="26"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
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
                  :class="{ 'border border-red-500': v$.form.username.$error }"
                  placeholder="john_doe"
                />
                <span class="error-span text-red-500" v-for="error in v$.form.username.$errors" :key="error">
                  {{ error.$message }}
                </span>
              </div>
              <div class="my-5 text-sm">
                <label for="password" class="flex text-lg">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="26"
                    height="26"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="mr-2"
                  >
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                  Password
                  <span class="text-red-500 mx-1">*</span>
                </label>

                <div class="relative w-full">
                  <div class="absolute inset-y-0 right-0 flex items-center px-1 py-3">
                    <button
                      class="rounded px-2 py-1 mt-11 text-sm hover:rounded-md cursor-pointer"
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
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                        <circle cx="12" cy="12" r="3"></circle>
                        <title>show/hide password</title>
                      </svg>
                    </button>
                  </div>
                </div>

                <input
                  :type="[showPass ? 'text' : 'password']"
                  class="form-input"
                  v-model="v$.form.password.$model"
                  :class="{ 'border border-red-500': v$.form.password.$error }"
                />
                <span class="error-span text-red-500" v-for="error in v$.form.password.$errors" :key="error">
                  {{ error.$message }}
                </span>
              </div>
            </form>
          </div>
          <!--footer-->
          <div class="p-3 mt-2 text-center space-x-4 md:block">
            <button
              class="text-center border-0 p-3 duration-300 hover:bg-green-500 hover:text-white rounded-full w-auto shadow-xl"
              :title="[isEditorMode ? 'Update' : 'Create']"
              @click.prevent="submitForm"
            >
              <svg
                v-if="!isEditorMode"
                xmlns="http://www.w3.org/2000/svg"
                width="40"
                height="40"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>

              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                width="40"
                height="40"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M2.5 2v6h6M21.5 22v-6h-6" />
                <path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapActions } from "vuex";

import useVuelidate from "@vuelidate/core";
import { required, url } from "@vuelidate/validators";
import { parse } from "tldts";

export default {
  name: "PasswordModal",
  components: {},
  props: {
    showModal: {
      type: Boolean,
      default: false,
    },

    isEditorMode: {
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
  emits: ["update:showModal"],

  data() {
    return {
      v$: useVuelidate(),
      form: {
        pid: this.pid,
        site: this.site,
        link: this.link,
        username: this.username,
        password: this.password,
      },

      showPass: false,
    };
  },

  validations() {
    return {
      form: {
        site: { required },
        link: { required, url },
        username: { required },
        password: { required },
      },
    };
  },

  methods: {
    ...mapActions(["createPassword", "updatePassword"]),

    async submitForm() {
      await this.v$.$validate();
      if (!this.v$.$invalid) {
        const passwordObj = Object.assign({}, this.form);
        // this.$emit("newPassword", this.form);
        if (this.isEditorMode) {
          // edit mode --> update
          await this.updatePassword(passwordObj);
        } else {
          delete passwordObj["pid"];
          await this.createPassword(passwordObj);
        }
        this.form = {};
        this.$emit("update:showModal", !this.showModal);
        this.v$.$reset();
      }
    },

    autoFillSite() {
      const result = parse(this.form.link);
      this.form.site = result.domainWithoutSuffix || result.domain;
    },

    emitCloseInternal() {
      this.v$.$reset();
      this.$emit("update:showModal", !this.showModal);
    },
  },
  updated() {
    this.form.pid = this.pid;
    this.form.site = this.site;
    this.form.link = this.link;
    this.form.username = this.username;
    this.form.password = this.password;
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