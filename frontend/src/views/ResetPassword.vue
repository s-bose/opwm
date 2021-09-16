  <template>
  <div>
    <div class="min-h-screen py-24">
      <div class="bg-dark-secondary w-10/12 sm:w-10/12 md:w-6/12 lg:w-4/12 pb-10 m-auto shadow-lg rounded-2xl text-white">
        <div class="py-8 px-8 rounded-xl">
          <h1 class="font-medium text-2xl mt-3 text-center">Reset Password</h1>
          <form action="" class="mt-6">
            <div class="my-7 text-sm">
              <label for="email" class="block text-lg">Email</label>
              <input
                type="text"
                id="email"
                autofocus
                class="form-input"
                placeholder="Email"
                v-model.trim="v$.form.email.$model"
                :class="{ 'border border-red-500': v$.form.email.$error }"
              />
            </div>

            <span class="error-span text-red-500" v-for="error in v$.form.email.$errors" :key="error">
              {{ error.$message }}
            </span>

            <div class="my-7 text-sm">
              <label for="password" class="block text-lg">Old Master Password </label>
              <div class="relative w-full">
                <div class="absolute inset-y-0 right-0 flex items-center px-2">
                  <button
                    class="hover:bg-gray-500 rounded px-1 py-1 mt-3 text-sm hover:rounded-md cursor-pointer"
                    id="toggle"
                    type="button"
                    @mouseup="showPass1 = !showPass1"
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
                  :type="[showPass1 ? 'text' : 'password']"
                  id="password"
                  class="form-input"
                  placeholder="Password"
                  v-model="v$.form.old_password.$model"
                  :class="{ 'border border-red-500': v$.form.old_password.$error }"
                />
              </div>
            </div>

            <span class="error-span text-red-500" v-for="error in v$.form.old_password.$errors" :key="error">
              {{ error.$message }}
            </span>

            <div class="my-7 text-sm">
              <label for="password" class="block text-lg">New Master Password </label>
              <div class="relative w-full">
                <div class="absolute inset-y-0 right-0 flex items-center px-2">
                  <button
                    class="hover:bg-gray-500 rounded px-1 py-1 mt-3 text-sm hover:rounded-md cursor-pointer"
                    id="toggle"
                    type="button"
                    @mouseup="showPass2 = !showPass2"
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
                  :type="[showPass2 ? 'text' : 'password']"
                  id="password"
                  class="form-input"
                  placeholder="Password"
                  v-model="v$.form.new_password.$model"
                  :class="{ 'border border-red-500': v$.form.new_password.$error }"
                />
              </div>
            </div>

            <span class="error-span text-red-500" v-for="error in v$.form.new_password.$errors" :key="error">
              {{ error.$message }}
            </span>

            <button class="block text-center text-gray-200 bg-gray-600 p-3 duration-300 rounded-md hover:bg-black w-full" @click.prevent="submitReset">
              Reset Password
            </button>
          </form>
        </div>
      </div>
    </div>

    <toast v-model:showToast="showToast" :info="serverError" :danger="true" />
  </div>
</template>


<script>
import { mapActions } from "vuex";

import useVuelidate from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";

import Toast from "../components/ToastComponent.vue";
export default {
  name: "Reset",
  components: { Toast },

  data() {
    return {
      v$: useVuelidate(),
      showToast: false,
      serverError: "",

      showPass0: false,
      showPass2: false,

      form: {
        email: "",
        old_password: "",
        new_password: "",
      },
    };
  },

  validations() {
    return {
      form: {
        email: { required, email },
        old_password: { required },
        new_password: { required },
      },
    };
  },

  methods: {
    ...mapActions(["resetPasswords", "logOut"]),

    async submitReset() {
      await this.v$.$validate();
      if (this.v$.invalid) {
        console.error(this.v$.$errors);
      } else {
        try {
          let resetForm = Object.assign({}, this.form);
          await this.resetPasswords(resetForm);

          await this.logOut();
          this.$router.push("/login");
        } catch (error) {
          this.serverError = error.response.data.detail;

          this.showToast = !this.showToast;
          setTimeout(() => {
            this.showToast = false;
          }, 1000);
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