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
            <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="8.5" cy="7" r="4"></circle>
            <line x1="20" y1="8" x2="20" y2="14"></line>
            <line x1="23" y1="11" x2="17" y2="11"></line>
          </svg>
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
                v-model="v$.password.password.$model"
                :class="[
                  passwordStrength == 0 || v$.password.password.$error
                    ? 'border border-red-500'
                    : passwordStrength == 1
                    ? 'border border-yellow-500'
                    : passwordStrength == 2
                    ? 'border border-blue-500'
                    : passwordStrength >= 3
                    ? 'border border-green-500'
                    : '',
                ]"
              />
            </div>

            <span class="error-span text-red-500" v-for="error in v$.password.password.$errors" :key="error">
              {{ error.$message }}
            </span>
            <span
              v-if="passwordStrength >= 0 && !isLogin"
              class="error-span"
              :class="{
                'text-red-500': passwordStrength == 0,
                'text-yellow-500': passwordStrength == 1,
                'text-blue-500': passwordStrength == 2,
                'text-green-500': passwordStrength >= 3,
              }"
            >
              Strength -
              {{ passwordStrength == 0 ? "weak" : passwordStrength == 1 ? "medium" : passwordStrength == 2 ? "strong" : "very strong" }}
            </span>
          </div>

          <div class="my-7 text-sm pb-5">
            <label for="confirm-password" class="block text-lg">Confirm Master Password</label>
            <input
              type="password"
              id="confirm-password"
              class="form-input"
              placeholder="Confirm password"
              v-model="v$.password.confirm.$model"
              :class="[v$.password.confirm.$model !== '' ? [v$.password.confirm.$error ? 'border border-red-500' : 'border border-green-500'] : '']"
            />

            <span class="error-span text-red-500" v-if="v$.password.confirm.$error"> Passwords do not match ! </span>
          </div>

          <button class="block text-center text-gray-200 bg-gray-600 p-3 duration-300 rounded-md hover:bg-black w-full" @click.prevent="submitSignup">
            Sign Up
          </button>
        </form>

        <div class="flex md:justify-between justify-center items-center mt-10">
          <div style="height: 1px" class="bg-gray-700 md:block hidden w-4/12"></div>
          <button class="md:mx-2 text-sm font-light hover:underline text-gray-400" @click.prevent="$router.push('/login')">Login</button>
          <div style="height: 1px" class="bg-gray-700 md:block hidden w-4/12"></div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src

import zxcvbn from "zxcvbn";

import useVuelidate from "@vuelidate/core";
import { required, email, minLength, sameAs } from "@vuelidate/validators";

export default {
  name: "Signup",
  components: {},
  props: {
    isLogin: {
      type: Boolean,
      default: false,
    },
  },

  data() {
    return {
      v$: useVuelidate(), // vuelidate obj

      email: "",
      password: {
        password: "",
        confirm: "",
      },
      showPass: false,
      passwordStrength: -1,
    };
  },
  validations() {
    return {
      email: { required, email },
      password: {
        password: { required, minLength: minLength(8) }, // master pwd minimum 8 characters
        confirm: {
          required,
          minLength: minLength(8),
          sameAsPassword: sameAs(this.password.password),
        },
      },
    };
  },

  updated() {
    // hook to validate on every form update
    this.passwordStrength = this.v$.password.password.$model !== "" ? zxcvbn(this.v$.password.password.$model).score : -1;

    // this.v$.$validate;   // NOTE: vuelidate model binding already does live validation, no need for this
  },

  methods: {
    // toggleSignup() {
    //   // login / signup toogle
    //   this.isLogin = !this.isLogin;
    //   this.email = "";
    //   this.password.password = "";
    //   this.password.confirm = "";
    //   this.v$.$reset(); // reset form entries on toggle
    // },
    async submitSignup() {
      await this.v$.$validate();
      if (this.v$.$invalid) {
        console.log(this.v$.$errors);
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


