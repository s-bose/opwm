<template>
  <!-- <div id="nav">
    <router-link to="/">Login</router-link> | <router-link to="/home">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <router-view v-slot="{ Component }">
    <transition name="router-fade">
      <component :is="Component" />
    </transition>
  </router-view>
</template>


<style scoped lang="postcss">
.router-fade-enter-active,
.router-fade-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.router-fade-enter-from,
.router-fade-leave-to {
  opacity: 0;
}
</style>