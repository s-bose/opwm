<template>
  <div class="container bg-white m-auto my-10 shadow-2xl rounded-2xl">
    <div class="py-8 px-8 relative overflow-hidden">
      <transition name="fade">
        <div
          class="
            bg-gradient
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
            rounded-2xl
            z-10
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
        <a :href="link" @click="redirectUrl">{{ link }}</a>
      </div>

      <form action="" class="mt-6">
        <div class="my-5 text-sm">
          <label for="username" class="block text-black text-lg">
            Username
          </label>
          <div class="relative w-full">
            <div class="absolute inset-y-0 right-0 flex items-center px-2">
              <button
                class="
                  hover:bg-gray-200
                  rounded
                  px-1
                  py-1
                  mt-12
                  text-sm text-gray-600
                  hover:rounded-md
                  cursor-pointer
                "
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
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path
                    d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"
                  ></path>
                  <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                </svg>
              </button>
            </div>
          </div>
          <input
            type="text"
            readonly
            autofocus
            class="
              appearance-none
              bg-transparent
              border-0 border-b-2 border-green-400
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
          <label for="password" class="block text-black text-lg">
            Password
          </label>

          <div class="relative w-full">
            <div class="absolute inset-y-0 right-0 flex items-center px-2">
              <button
                class="
                  hover:bg-gray-200
                  rounded
                  px-2
                  py-1
                  mt-12
                  text-sm text-gray-600
                  hover:rounded-md
                  cursor-pointer
                "
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
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
              </button>

              <button
                class="
                  hover:bg-gray-200
                  rounded
                  px-2
                  py-1
                  mt-12
                  text-sm text-gray-600
                  hover:rounded-md
                  cursor-pointer
                "
                type="button"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path
                    d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"
                  ></path>
                  <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                </svg>
              </button>
            </div>
          </div>

          <input
            :type="[showPass ? 'text' : 'password']"
            readonly
            class="
              appearance-none
              bg-transparent
              border-0 border-b-2 border-green-400
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
              border-0
              p-3
              duration-300
              hover:bg-green-900
              hover:border-green-500
              hover:text-white
              rounded-full
              shadow-xl
              w-2/4
            "
          >
            Edit
          </button>
          <button
            class="
              text-center text-black
              border-0
              p-3
              duration-300
              hover:bg-red-900
              hover:text-white
              rounded-full
              w-2/4
              shadow-xl
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
      showPass: false,
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
        const pair = (() => {
          let x1 = hexCols[Math.round(Math.random() * (hexCols.length - 1))];
          let x2 = hexCols[Math.round(Math.random() * (hexCols.length - 1))];
          return x1 + x2;
        })();

        // for (let i = 0; i < 3; i++) {
        //   a += pair;
        // }
        a += "50";
        a += pair;
        a += "89";
        return a;
      };

      let grad1 = populate("#");
      let grad2 = populate("#");

      let gradient =
        "linear-gradient(" + 180 + "deg, " + grad1 + "," + grad2 + ")";
      return gradient;
    },
    redirectUrl() {
      window.open(this.link);
    },
  },

  mounted() {
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

.bg-gradient {
  background: linear-gradient(180deg, #f9fafb, #6b7280);
}
</style>