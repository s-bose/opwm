<template>
  <div class="container-fluid h-full bg-gray-300">
    <h1 class="font-medium text-5xl mt-3 antialiased">This is Home</h1>
    <div
      class="
        container-fluid
        items-center
        mx-4
        h-full
        grid grid-cols-1
        sm:grid-cols-2
        md:grid-cols-2
        lg:grid-cols-2
        xl:grid-cols-3
        transition
        gap-5
      "
    >
      <Password
        v-for="entry in entries"
        :key="entry.id"
        :site="entry.site"
        :link="entry.link"
        :username="entry.username"
        :password="entry.password"
      />
    </div>
  </div>
</template>

<script>
import Password from "../components/Password.vue";

export default {
  name: "Home",
  components: { Password },

  data() {
    return {
      entries: [
        {
          site: "Google",
          link: "http://www.google.com",
          username: "joe",
          password: "mamma",
        },
        {
          site: "Youtube",
          link: "http://www.youtube.com",
          username: "david32",
          password: "cumbucket69",
        },
        {
          site: "Facebook",
          link: "http://www.facebook.com",
          username: "nigga69420",
          password: "urmomEatsAss69",
        },
        {
          site: "Mega",
          link: "http://www.mega.nz",
          username: "dude_the_legend",
          password: "xxx_tentacion_xxx",
        },
        {
          site: "Twitter",
          link: "http://www.twitter.com",
          username: "donald_drump",
          password: "tronald_dump",
        },
        {
          site: "Reddit",
          link: "http://www.reddit.com",
          username: "cummy_bot",
          password: "real_cummy_bot_65",
        },
      ],
    };
  },
};
</script>

<style>
</style>