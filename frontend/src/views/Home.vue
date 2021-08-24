<template>
  <div class="container-fluid h-full bg-white">
    <div class="p-8">
      <div class="bg-white flex items-center rounded-full shadow-xl">
        <input
          class="
            rounded-l-full
            w-full
            py-6
            px-6
            text-gray-500
            leading-tight
            focus:outline-none
          "
          id="search"
          type="text"
          placeholder="Search..."
          v-model="searchItem"
        />

        <div class="p-4">
          <button
            class="
              text-black
              p-2
              bg-none
              focus:outline-none
              w-auto
              h-auto
              flex
              items-center
              justify-center
              shadow-xl
            "
          ></button>
        </div>
      </div>
    </div>

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
        2xl:grid-cols-4
        transition
        gap-5
      "
    >
      <Password
        v-for="(entry, index) in matchSearchItem"
        :key="index"
        :site="entry.site"
        :link="entry.link"
        :username="entry.username"
        :password="entry.password"
        @click="toggleCard(index)"
        :show="isActive === index"
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
      isActive: null,
      searchItem: "",
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

  methods: {
    toggleCard(index) {
      this.isActive = index;
    },
  },

  computed: {
    matchSearchItem() {
      if (this.searchItem === "") {
        return this.entries;
      } else {
        return this.entries.filter((entry) => entry.site === this.searchItem);
      }
    },
  },
};
</script>

<style>
.body-bg {
  background: linear-gradient(180deg, #34e89e 0%, #0f3443 100%);
}

/* -----
SVG Icons - svgicons.sparkk.fr
----- */

.svg-icon {
  width: 1em;
  height: 1em;
}

.svg-icon path,
.svg-icon polygon,
.svg-icon rect {
  fill: #4691f6;
}

.svg-icon circle {
  stroke: #4691f6;
  stroke-width: 1;
}
</style>