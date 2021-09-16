<template>
  <div></div>
</template>

<script>
export default {
  name: "root",
  computed: {
    isLoggedIn() {
      return this.$store.getters.isAuthenticated;
    },
  },

  created() {
    console.log(this.isLoggedIn);
    if (this.isLoggedIn) {
      this.$router.push("/home");
    } else {
      this.$router.push("/login");
    }
  },
};
</script>

<style>
</style>