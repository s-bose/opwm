<template>
  <div class="min-h-screen py-24">
    <div class="bg-dark-secondary w-10/12 sm:w-10/12 md:w-6/12 lg:w-4/12 pb-10 m-auto shadow-lg rounded-2xl text-white">
      <div class="py-8 px-8 rounded-xl text-center">
        <button
          class="
            text-green-700
            bg-transparent
            border border-solid border-green-700
            hover:border-green-500
            hover:text-green-800
            font-bold
            uppercase
            px-3
            py-3
            rounded
            outline-none
            focus:outline-none
            mr-1
            mb-1
            rounded-full
            ease-linear
            transition-all
            duration-150
          "
          type="button"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="120"
            height="120"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="m-auto p-auto"
          >
            <path d="M5.52 19c.64-2.2 1.84-3 3.22-3h6.52c1.38 0 2.58.8 3.22 3" />
            <circle cx="12" cy="10" r="3" />
            <circle cx="12" cy="12" r="10" />
          </svg>
        </button>

        <div class="grid grid-cols-4 gap-8 mt-8 mx-8">
          <div class="bg-dark-secondary flex items-center justify-center rounded-sm shadow-xl col-span-1">
            <label for="name" class="block text-lg">Name</label>
          </div>
          <div class="col-start-2 col-span-3">
            <input type="text" id="name" autofocus class="form-input" placeholder="Name" :value="details.name" />
          </div>

          <div class="bg-dark-secondary flex items-center justify-center rounded-sm shadow-xl col-span-1">
            <label for="email" class="block text-lg">Email</label>
          </div>
          <div class="col-start-2 col-span-3">
            <input type="text" id="email" autofocus class="form-input" placeholder="Email" :value="details.email" />
          </div>

          <div class="bg-dark-secondary flex items-center justify-center rounded-sm shadow-xl col-span-1">
            <label for="password" class="block text-lg">Password</label>
          </div>
          <div class="col-start-2 col-span-3">
            <input type="password" id="password" autofocus class="form-input" :value="details.password" />
          </div>

          <!-- reset password and delete account -->

          <button class="text-center border-0 p-3 duration-300 hover:bg-green-900 hover:text-white rounded-full shadow-xl col-span-2">Reset Password</button>

          <button class="text-center border-0 p-3 duration-300 hover:bg-red-900 hover:text-white rounded-full shadow-xl col-span-2">Delete Account</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  name: "About",
  data() {
    return {
      displayToast: false,

      details: {
        name: "Jeff_bezos",
        email: "jeffbezos@amazon.com",
        password: "iamjeffbezos",
      },
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

<style scoped lang="postcss">
.fade-pop-enter-active,
.fade-pop-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-pop-enter-from,
.fade-pop-leave-to {
  opacity: 0;
}

.form-input {
  @apply rounded-md
          px-4
          py-3
          m-auto
          focus:outline-none
          bg-gray-100
          w-full
          bg-dark-primary;
}
</style>