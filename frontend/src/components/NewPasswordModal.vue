<template>
  <div
    class="
      min-w-screen
      h-screen
      animated
      fadeIn
      faster
      fixed
      left-0
      top-0
      flex
      justify-center
      items-center
      inset-0
      z-50
      outline-none
      focus:outline-none
      bg-no-repeat bg-center bg-cover
    "
    id="modal-id"
  >
    <div class="absolute bg-black opacity-80 inset-0 z-0"></div>
    <div
      class="
        w-full
        max-w-lg
        p-5
        relative
        mx-auto
        my-auto
        rounded-xl
        shadow-lg
        bg-white
      "
    >
      <!--content-->
      <div class="content">
        <!--body-->
        <div class="p-5 flex-auto justify-center">
          <h2 class="text-2xl text-center font-bold py-4">
            Create new Password
          </h2>
          <form action="" class="mt-6">
            <div class="my-5 text-sm">
              <label for="site" class="flex text-black text-lg"
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <circle cx="12" cy="12" r="10"></circle>
                </svg>
                Site
              </label>
              <div class="relative w-full"></div>
              <input
                type="text"
                autofocus
                class="form-input"
                v-model="site"
                placeholder="ex: google"
              />
            </div>
            <div class="my-5 text-sm">
              <label for="link" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <path
                    d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"
                  ></path>
                  <path
                    d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"
                  ></path>
                </svg>
                Link
              </label>
              <div class="relative w-full"></div>
              <input
                type="text"
                autofocus
                class="form-input"
                v-model="link"
                placeholder="www.example.com"
              />
            </div>

            <div class="my-5 text-sm">
              <label for="username" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                Username
              </label>
              <div class="relative w-full"></div>
              <input
                type="text"
                autofocus
                class="form-input"
                v-model="username"
                placeholder="john_doe"
              />
            </div>
            <div class="my-5 text-sm">
              <label for="password" class="flex text-black text-lg">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="26"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="mr-2"
                >
                  <rect
                    x="3"
                    y="11"
                    width="18"
                    height="11"
                    rx="2"
                    ry="2"
                  ></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
                Password
              </label>

              <div class="relative w-full">
                <div
                  class="absolute inset-y-0 right-0 flex items-center px-1 py-3"
                >
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
                      <path
                        d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"
                      ></path>
                      <circle cx="12" cy="12" r="3"></circle>
                    </svg>
                  </button>
                </div>
              </div>

              <input
                :type="[showPass ? 'text' : 'password']"
                class="form-input"
                v-model="password"
              />
            </div>
          </form>
        </div>
        <!--footer-->
        <div class="p-3 mt-2 text-center space-x-4 md:block">
          <button
            class="
              text-center text-black
              border-0
              p-3
              duration-300
              hover:bg-green-500
              hover:text-white
              rounded-full
              w-auto
              shadow-xl
            "
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="40"
              height="40"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#000000"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PasswordModal",
  components: {},
  data() {
    return {
      site: "",
      link: "",
      username: "",
      password: "",
      showPass: false,
    };
  },

  updated() {
    console.log("hello");
    console.log(this.password);
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
          border;
}
</style>
