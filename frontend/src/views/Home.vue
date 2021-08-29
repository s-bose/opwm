<template>
  <div class="container-fluid relative h-full bg-dark-primary">
    <div class="p-8">
      <div class="bg-dark-secondary flex items-center rounded-full shadow-xl">
        <input
          class="rounded-l-full w-full bg-dark-secondary py-6 px-6 text-white leading-tight focus:outline-none"
          id="search"
          type="text"
          placeholder="Search..."
          v-model="searchItem"
        />

        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="#FFFFFF"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="mr-5"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>

        <!-- <div class="p-4">
          <button class="text-black p-2 bg-none focus:outline-none w-auto h-auto flex items-center justify-center shadow-xl"></button>
        </div> -->
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
      ref="outer"
      @click.prevent="clickOutside"
    >
      <Password
        v-for="(entry, index) in matchSearchItem"
        :ref="
          (el) => {
            pwds[index] = el;
          }
        "
        :key="index"
        :site="entry.site"
        :link="entry.link"
        :username="entry.username"
        :password="entry.password"
        @click.prevent="toggleCard(index)"
        :show="isActive === index"
      />
    </div>

    <div class="container modal-button">
      <button
        class="
          fixed
          z-20
          bottom-10
          right-10
          p-0
          w-16
          h-16
          bg-green-600
          rounded-full
          hover:bg-gray-800
          shadow-lg
          active:shadow-lg
          mouse
          shadow
          transition
          ease-in
          duration-200
          focus:outline-none
        "
        @click.prevent="showModal = !showModal"
      >
        <svg viewBox="0 0 20 20" enable-background="new 0 0 20 20" class="w-6 h-6 inline-block">
          <path
            fill="#FFFFFF"
            d="M16,10c0,0.553-0.048,1-0.601,1H11v4.399C11,15.951,10.553,16,10,16c-0.553,0-1-0.049-1-0.601V11H4.601
                                    C4.049,11,4,10.553,4,10c0-0.553,0.049-1,0.601-1H9V4.601C9,4.048,9.447,4,10,4c0.553,0,1,0.048,1,0.601V9h4.399
                                    C15.952,9,16,9.447,16,10z"
          />
        </svg>
      </button>

      <password-modal v-model:showModal="showModal" @newPassword="addNewPassword" />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

import Password from "../components/PasswordComponent.vue";
import PasswordModal from "../components/PasswordModalComponent.vue";
export default {
  name: "Home",
  components: { Password, PasswordModal },
  setup() {
    const pwds = ref([]);
    return { pwds };
  },
  data() {
    return {
      isActive: null,
      searchItem: "",
      showModal: false,

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
    addNewPassword(e) {
      this.entries.push(e);
    },
  },

  computed: {
    matchSearchItem() {
      if (this.searchItem === "") {
        return this.entries;
      } else {
        return this.entries.filter((entry) => entry.site.toLowerCase().includes(this.searchItem.toLowerCase()));
      }
    },
  },
  mounted() {
    document.addEventListener("click", (e) => {
      e.preventDefault();
      if (this.isActive !== null && !this.pwds[this.isActive].$el.contains(e.target)) {
        this.isActive = null;
      }
    });
  },
};
</script>

<style>
.body-bg {
  background: linear-gradient(180deg, #34e89e 0%, #0f3443 100%);
}

.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
}
</style>