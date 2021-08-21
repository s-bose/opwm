<template>
  <div class="body-bg min-h-screen py-24">
    <div
      class="
        bg-white
        dark:bg-black
        w-10/12
        sm:w-10/12
        md:w-6/12
        lg:w-4/12
        pb-10
        m-auto
        shadow-lg
        rounded-lg
        dark:text-white
      "
    >
      <div class="py-8 px-8 rounded-xl">
        <h1 class="font-medium text-2xl mt-3 text-center">
          {{ isLogin ? "Login" : "Sign Up" }}
        </h1>
        <form action="" class="mt-6">
          <div class="my-7 text-sm">
            <label for="email" class="block text-black">Email</label>
            <input
              type="text"
              id="email"
              autofocus
              class="form-input"
              placeholder="Email"
              v-model.trim="v$.email.$model"
              :class="{ 'border-red-500': v$.email.$error }"
            />

            <span v-if="v$.email.$error" class="error-span text-red-500">
              Invalid email address !
            </span>
          </div>

          <div class="my-7 text-sm">
            <label for="password" class="block text-black"> Master Password </label>
            <div class="relative w-full">
              <div class="absolute inset-y-0 right-0 flex items-center px-2">
                <button
                  class="
                    hover:bg-gray-200
                    rounded
                    px-1
                    py-1
                    mt-3
                    text-sm text-gray-600
                    hover:rounded-md
                    cursor-pointer
                  "
                  id="toggle"
                  type="button"
                  @mouseup="showPass = !showPass"
                  @mousedown="showPass = !showPass"
                >
                  {{ showPass ? "hide" : "show" }}
                </button>
              </div>

              <input
                :type="[showPass ? 'text' : 'password']"
                id="password"
                class="form-input"
                placeholder="Password"
                v-model="v$.password.password.$model"
                :class="[
                  !isLogin
                    ? [
                        passwordStrength == 0 || v$.password.password.$error
                          ? 'border-red-500'
                          : passwordStrength == 1
                          ? 'border-yellow-500'
                          : passwordStrength == 2
                          ? 'border-blue-500'
                          : passwordStrength >= 3
                          ? 'border-green-500'
                          : '',
                      ]
                    : '',
                ]"
              />
            </div>

            <span
              v-if="v$.password.password.$error && !isLogin"
              class="error-span text-red-500"
            >
              Password must be atleast 8 characters long !
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
              {{
                passwordStrength == 0
                  ? "weak"
                  : passwordStrength == 1
                  ? "medium"
                  : passwordStrength == 2
                  ? "strong"
                  : "very strong"
              }}
            </span>

            <div class="flex justify-end mt-2 text-xs text-gray-600" v-if="isLogin">
              <a href="">Forgot Password?</a>
            </div>
          </div>

          <div class="my-7 text-sm pb-5" v-if="!isLogin">
            <label for="confirm-password" class="block text-black"
              >Confirm Master Password</label
            >
            <input
              type="password"
              id="confirm-password"
              class="form-input"
              placeholder="Confirm password"
              v-model="v$.password.confirm.$model"
              :class="[
                v$.password.confirm.$model !== ''
                  ? [v$.password.confirm.$error ? 'border-red-500' : 'border-green-500']
                  : '',
              ]"
            />

            <span class="error-span text-red-500" v-if="v$.password.confirm.$error">
              Passwords do not match !
            </span>
          </div>

          <button
            class="
              block
              text-center text-white
              bg-gray-800
              p-3
              duration-300
              rounded-md
              hover:bg-black
              w-full
            "
          >
            {{ isLogin ? "Login" : "Sign Up" }}
          </button>
        </form>

        <div class="flex md:justify-between justify-center items-center mt-10">
          <div style="height: 1px" class="bg-gray-300 md:block hidden w-4/12"></div>
          <button
            class="md:mx-2 text-sm font-light hover:underline text-gray-400"
            @click.prevent="toggleSignup"
          >
            {{ isLogin ? "Create an account" : "Login" }}
          </button>
          <div style="height: 1px" class="bg-gray-300 md:block hidden w-4/12"></div>
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
  name: "Home",
  components: {},

  data() {
    return {
      v$: useVuelidate(), // vuelidate obj

      isLogin: true,
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
    this.passwordStrength =
      this.v$.password.password.$model !== ""
        ? zxcvbn(this.v$.password.password.$model).score
        : -1;

    this.v$.$validate;
  },

  methods: {
    toggleSignup() {
      // login / signup toogle
      this.isLogin = !this.isLogin;
      this.email = "";
      this.password.password = "";
      this.password.confirm = "";

      this.v$.$reset(); // reset form entries on toggle
    },
  },
};
</script>

<style scoped lang="postcss">
.body-bg {
  background: linear-gradient(180deg, #34e89e 0%, #0f3443 100%);
}

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
</style>
