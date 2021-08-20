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
            <label
              for="email"
              class="block text-black"
              :class="{ 'text-red-500': v$.email.$error }"
              >Email</label
            >
            <input
              type="text"
              id="email"
              autofocus
              class="
                rounded-md
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
                border
              "
              placeholder="Email"
              v-model.trim="v$.email.$model"
              :class="{ 'border-red-500': v$.email.$error }"
            />
          </div>

          <div class="my-7 text-sm">
            <label for="password" class="block text-black"
              >Master Password</label
            >
            <input
              type="password"
              id="password"
              class="
                rounded-md
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
              "
              placeholder="Password"
              v-model="password.password"
            />

            <div
              class="flex justify-end mt-2 text-xs text-gray-600"
              v-if="isLogin"
            >
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
              class="
                rounded-md
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
              "
              placeholder="Confirm password"
              v-model="password.confirm"
            />
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
          <div
            style="height: 1px"
            class="bg-gray-300 md:block hidden w-4/12"
          ></div>
          <button
            class="md:mx-2 text-sm font-light hover:underline text-gray-400"
            @click.prevent="onCreateAcc"
          >
            {{ isLogin ? "Create an account" : "Login" }}
          </button>
          <div
            style="height: 1px"
            class="bg-gray-300 md:block hidden w-4/12"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import useVuelidate from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";

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
    };
  },
  validations() {
    return {
      email: { required, email },
      password: {
        password: "",
        confirm: "",
      },
    };
  },

  methods: {
    // onchange email and password validation, use vuelidate & zxcvbn
    test() {
      console.log(this.v$.email.$model);
    },
    onCreateAcc() {
      this.isLogin = !this.isLogin;
      this.email = "";
      this.password.password = "";
      this.password.confirm = "";
    },
  },

  updated() {
    console.log(!this.v$.email.$error);
    this.v$.$validate;
  },
};
</script>

<style scoped>
.body-bg {
  background: linear-gradient(180deg, #34e89e 0%, #0f3443 100%);
}

.form-group--error {
  border: 1px solid red;
}
</style>
