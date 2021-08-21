<template>
  <div class="bg-white lg:w-4/12 md:6/12 w-10/12 m-auto my-10 shadow-md">
    <div class="py-8 px-8 rounded-xl">
      <h1 class="font-medium text-2xl mt-3 antialiased">{{ site }}</h1>
      <div class="underline mt-2 text-gray-600 hover:text-gray-800">
        <a :href="link">{{ link }}</a>
      </div>

      <form action="" class="mt-6">
        <div class="my-5 text-sm">
          <label for="username" class="block text-black">Username</label>
          <input
            type="text"
            readonly
            autofocus
            id="username"
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
            id="password"
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
              rounded-sm
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
              rounded-sm
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
  name: "Passwords",
  components: {},

  props: {
    site: String,
    link: String,
    username: String,
    password: String,
  },
};
</script>

<style>
</style>