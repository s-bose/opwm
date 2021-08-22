<template>
  <div class="container bg-white m-auto my-10 shadow-md">
    <div class="py-8 px-8 relative overflow-hidden">
      <transition name="fade">
        <div
          class="
            text-white
            h-full
            w-full
            absolute
            inset-0
            cursor-pointer
            delay-50
            text-center
            content-center
            flex
          "
          :style="{ background: gradient }"
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
          <label for="username" class="block text-black text-lg"
            >Username</label
          >
          <input
            type="text"
            readonly
            autofocus
            class="
              appearance-none
              bg-transparent
              border-0 border-b-2 border-indigo-300
              px-4
              py-3
              mt-3
              focus:outline-none
              w-full
              leading-tight
            "
            :value="username"
          />
        </div>
        <div class="my-5 text-sm">
          <label for="password" class="block text-black text-lg"
            >Password</label
          >
          <input
            type="password"
            readonly
            class="
              appearance-none
              bg-transparent
              border-0 border-b-2 border-indigo-300
              px-4
              py-3
              mt-3
              focus:outline-none
              w-full
              leading-tight
            "
            :value="password"
          />
        </div>
        <div class="grid md:grid-cols-2 gap-10 mt-12 justify-items-center">
          <button
            class="
              text-center text-black
              border-0 border-b-2
              p-3
              duration-300
              hover:bg-green-900
              hover:border-green-500
              hover:text-white
              w-2/4
            "
          >
            Edit
          </button>
          <button
            class="
              text-center text-black
              border-0 border-b-2
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
      gradient: "",
    };
  },

  props: {
    show: Boolean,
    site: String,
    link: String,
    username: String,
    password: String,
  },

  methods: {
    generateGradBg() {
      const hexCols = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
      ];

      const populate = (a) => {
        for (let i = 0; i < 6; i++) {
          let x = Math.round(Math.random() * (hexCols.length - 1));
          a += hexCols[x];
        }
        return a;
      };

      let grad1 = populate("#");
      let grad2 = populate("#");
      let angle = Math.round(Math.random() * 360);

      let gradient =
        "linear-gradient(" + angle + "deg, " + grad1 + "," + grad2 + ")";
      return gradient;
    },
  },

  created() {
    this.gradient = this.generateGradBg();
  },
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