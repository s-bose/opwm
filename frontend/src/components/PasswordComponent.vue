<template>
  <div class="container bg-dark-secondary border-b-4 border-dark-accent text-white m-auto my-10 shadow-2xl rounded-2xl">
    <div class="py-8 px-8 relative overflow-hidden">
      <transition name="fade">
        <div
          class="
            bg-dark-primary
            text-white
            h-full
            w-full
            absolute
            inset-0
            cursor-pointer
            text-center
            content-center
            flex
            rounded-2xl
            z-10
            transition
            duration-300
            ease-in-out
            transform
            hover:-translate-y-5
          "
          v-if="!show"
        >
          <h1 class="font-large text-2xl m-auto antialiased">
            {{ site }}
          </h1>
        </div>
      </transition>
      <div id="card-body">
        <h1 class="font-medium text-2xl mt-3 antialiased">{{ site }}</h1>
        <div class="underline mt-2 hover:text-gray-300 text-xs">
          <a :href="link" @click="redirectUrl"
            ><p class="overflow-ellipsis overflow-hidden truncate">{{ link }}</p></a
          >
        </div>

        <form action="" class="mt-6">
          <div class="my-5 text-sm">
            <label for="username" class="block text-lg"> Username </label>
            <div class="relative w-full">
              <div class="absolute inset-y-0 right-0 flex items-center px-2">
                <button
                  class="hover:bg-gray-700 rounded px-1 py-1 mt-12 text-sm hover:rounded-md cursor-pointer"
                  type="button"
                  @click.prevent="copyClipboard(username)"
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
                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                  </svg>
                </button>
              </div>
            </div>
            <input
              type="text"
              readonly
              autofocus
              class="appearance-none bg-transparent border-0 border-b-2 border-dark-accent px-4 py-3 mt-3 focus:outline-none w-full leading-tight"
              :value="username"
            />
          </div>
          <div class="my-5 text-sm">
            <label for="password" class="block text-lg"> Password </label>

            <div class="relative w-full">
              <div class="absolute inset-y-0 right-0 flex items-center px-2">
                <button
                  class="hover:bg-gray-700 rounded px-2 py-1 mt-12 text-sm hover:rounded-md cursor-pointer"
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

                <button
                  class="hover:bg-gray-700 rounded px-2 py-1 mt-12 text-sm hover:rounded-md cursor-pointer"
                  type="button"
                  @click.prevent="copyClipboard(password)"
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
                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                  </svg>
                </button>
              </div>
            </div>

            <input
              :type="[showPass ? 'text' : 'password']"
              readonly
              class="appearance-none bg-transparent border-0 border-b-2 border-dark-accent px-4 py-3 mt-3 focus:outline-none w-full leading-tight"
              :value="password"
            />
          </div>
          <div class="grid md:grid-cols-2 gap-10 mt-12 justify-items-center">
            <button
              class="text-center border-0 p-3 duration-300 hover:bg-green-900 hover:border-green-500 hover:text-white rounded-full shadow-xl w-3/4"
              @click.prevent="openEditModal"
            >
              Edit
            </button>
            <button class="text-center border-0 p-3 duration-300 hover:bg-red-900 hover:text-white rounded-full w-3/4 shadow-xl" @click.prevent="openDelModal">
              Delete
            </button>
          </div>
        </form>
      </div>
      <transition name="fade-pop">
        <div class="fixed bottom-5 left-5 z-20" v-show="showToast">
          <div class="mb-5">
            <div class="flex w-full max-w-sm mx-auto overflow-hidden bg-dark-secondary rounded-lg shadow-md text-white">
              <div class="flex items-center justify-center w-12 bg-green-700">
                <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z"
                  />
                </svg>
              </div>

              <div class="px-4 py-2 -mx-3">
                <div class="mx-3">
                  <p class="text-md">Text copied to clipboard</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "Password",

  emits: ["OnEditPassword", "OnDelPassword"],
  data() {
    return {
      toggleCard: false,
      gradient: "",
      showPass: false,

      showEditorModal: false,

      showToast: false,
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
    redirectUrl() {
      window.open(this.link);
    },

    openEditModal() {
      this.$emit("OnEditPassword", this.$props);
    },

    openDelModal() {
      this.$emit("OnDelPassword", this.$props);
    },

    async copyClipboard(value) {
      await navigator.clipboard.writeText(value);
      this.showToast = !this.showToast;
      setTimeout(() => {
        this.showToast = false;
      }, 1000);
    },
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

.fade-pop-enter-active,
.fade-pop-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-pop-enter-from,
.fade-pop-leave-to {
  opacity: 0;
}
</style>