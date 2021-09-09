<template>
  <div class="min-h-screen py-24">
    <div class="bg-dark-secondary w-10/12 sm:w-10/12 md:w-6/12 lg:w-4/12 pb-10 m-auto shadow-lg rounded-2xl text-white">
      <div class="py-8 px-8 rounded-xl">
        <h1 class="font-medium text-2xl mt-3 text-center">
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
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M13.8 12H3" />
          </svg>
          <span class="m-auto p-auto text-lg text-red-500">{{ serverError }}</span>
        </h1>
        <form action="" class="mt-6">
          <div class="my-7 text-sm">
            <label for="email" class="block text-lg">Email</label>
            <input
              type="text"
              id="email"
              autofocus
              class="form-input"
              placeholder="Email"
              v-model.trim="v$.email.$model"
              :class="{ 'border border-red-500': v$.email.$error }"
            />

            <span v-if="v$.email.$error" class="error-span text-red-500"> Invalid email address ! </span>
          </div>

          <div class="my-7 text-sm">
            <label for="password" class="block text-lg"> Master Password </label>
            <div class="relative w-full">
              <div class="absolute inset-y-0 right-0 flex items-center px-2">
                <button
                  class="hover:bg-gray-500 rounded px-1 py-1 mt-3 text-sm hover:rounded-md cursor-pointer"
                  id="toggle"
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
                  </svg>
                </button>
              </div>

              <input
                :type="[showPass ? 'text' : 'password']"
                id="password"
                class="form-input"
                placeholder="Password"
                v-model="v$.password.$model"
                :class="{ 'border border-red-500': v$.password.$error }"
              />
            </div>
            <span class="error-span text-red-500" v-for="error in v$.password.$errors" :key="error">
              {{ error.$message }}
            </span>

            <div class="flex justify-end mt-2 text-xs text-gray-600">
              <a href="" class="hover:underline">Forgot Password?</a>
            </div>
          </div>

          <button class="block text-center text-gray-200 bg-gray-600 p-3 duration-300 rounded-md hover:bg-black w-full" @click.prevent="submitLogin">
            Login
          </button>
        </form>

        <div class="flex md:justify-between justify-center items-center mt-10">
          <div style="height: 1px" class="bg-gray-700 md:block hidden w-4/12"></div>
          <button class="md:mx-2 text-sm font-light hover:underline text-gray-400" @click.prevent="$router.push('/signup')">Sign Up</button>
          <div style="height: 1px" class="bg-gray-700 md:block hidden w-4/12"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

import useVuelidate from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";

export default {
  name: "Login",
  components: {},

  data() {
    return {
      v$: useVuelidate(), // vuelidate obj

      email: "",
      password: "",
      showPass: false,

      serverError: "",
    };
  },
  validations() {
    return {
      email: { required, email },
      password: { required },
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    async submitLogin() {
      await this.v$.$validate();
      if (this.v$.$invalid) {
        console.log(this.v$.$errors);
      } else {
        // submit the form

        try {
          let res = await this.logIn({ email: this.email, master_pwd: this.password });
          console.log(res);
          this.$router.push("/home");
        } catch (error) {
          this.serverError = error.response.data.detail;
        }
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
</style>