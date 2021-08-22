<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Password
      site="Google"
      link="http://www.google.com"
      username="john"
      password="doe"
    />
  </div>
</template>

<script>
import Password from "../components/Password.vue";

export default {
  name: "About",
  components: {
    Password,
  },
};
</script>
