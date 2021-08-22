<template>
  <div class="container bg-white m-auto my-10 shadow-md rounded-lg">
    <div class="py-8 px-8 relative overflow-hidden">
      <transition name="fade">
        <div
          class="
            bg-gray-400
            text-white
            h-full
            w-full
            absolute
            inset-0
            rounded-lg
            cursor-pointer
            delay-50
            text-center
            content-center
            flex
          "
          v-if="!show"
        >
          <h1 class="font-large text-2xl m-auto antialiased">
            {{ site }}
          </h1>
        </div>
      </transition>
      <h1 class="font-medium text-2xl mt-3 antialiased">{{ site }}</h1>
      <div class="underline mt-2 text-gray-600 hover:text-gray-800">
        <a href="">{{ link }}</a>
      </div>

      <form action="" class="mt-6">
        <div class="my-5 text-sm">
          <label for="username" class="block text-black">Username</label>
          <input
            type="text"
            readonly
            autofocus
            class="
              rounded-sm
              px-4
              py-3
              mt-3
              focus:outline-none
              bg-gray-100
              w-full
              border
            "
            :value="username"
          />
        </div>
        <div class="my-5 text-sm">
          <label for="password" class="block text-black">Password</label>
          <input
            type="password"
            readonly
            class="
              rounded-sm
              px-4
              py-3
              mt-3
              focus:outline-none
              bg-gray-100
              w-full
              border
            "
            :value="password"
          />
        </div>
        <div class="grid md:grid-cols-2 gap-10 mt-12 justify-items-center">
          <button
            class="
              text-center text-black
              border border-green-600
              p-3
              duration-300
              hover:bg-green-900
              hover:text-white
              w-2/4
            "
          >
            Edit
          </button>
          <button
            class="
              text-center text-black
              border border-red-700
              p-3
              duration-300
              hover:bg-red-900
              hover:text-white
              w-2/4
            "
          >
            Delete
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Password",
  components: {},

  data() {
    return {
      toggleCard: false,
    };
  },

  props: {
    show: Boolean,

    site: String,
    link: String,
    username: String,
    password: String,
  },

  methods: {},
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>