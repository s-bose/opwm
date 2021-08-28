<template>
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
      <input required type="text" autofocus class="form-input" v-model="form.site" placeholder="ex: google" />
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
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        Link
        <span class="text-red-500 mx-1">*</span>
      </label>
      <div class="relative w-full"></div>
      <input
        type="text"
        autofocus
        class="form-input"
        v-model="v$.form.link.$model"
        :class="{ 'border-red-500': v$.form.link.$error }"
        placeholder="www.example.com"
      />
      <span class="error-span text-red-500" v-for="error in v$.form.link.$errors" :key="error">
        {{ error.$message }}
      </span>
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
        <span class="text-red-500 mx-1">*</span>
      </label>
      <div class="relative w-full"></div>
      <input
        type="text"
        autofocus
        class="form-input"
        v-model="v$.form.username.$model"
        :class="{ 'border-red-500': v$.form.username.$error }"
        placeholder="john_doe"
      />
      <span class="error-span text-red-500" v-for="error in v$.form.username.$errors" :key="error">
        {{ error.$message }}
      </span>
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
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
        </svg>
        Password
        <span class="text-red-500 mx-1">*</span>
      </label>

      <div class="relative w-full">
        <div class="absolute inset-y-0 right-0 flex items-center px-1 py-3">
          <button
            class="hover:bg-gray-200 rounded px-2 py-1 mt-12 text-sm text-gray-600 hover:rounded-md cursor-pointer"
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
        </div>
      </div>

      <input
        :type="[showPass ? 'text' : 'password']"
        class="form-input"
        v-model="v$.form.password.$model"
        :class="{ 'border-red-500': v$.form.password.$error }"
      />
      <span class="error-span text-red-500" v-for="error in v$.form.password.$errors" :key="error">
        {{ error.$message }}
      </span>
    </div>
  </form>
</template>

<script>
export default {};
</script>

<style scoped lang="postcss">
</style>