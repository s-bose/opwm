<template>
  <div class="container-fluid relative h-full">
    <div class="p-8 grid grid-cols-3 gap-4">
      <div class="bg-dark-secondary flex items-center rounded-full shadow-xl col-span-2">
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
      </div>
      <div class="col-span-1 grid grid-cols-2 gap-4 text-white">
        <button class="nav-button" @click.prevent="logoutHandler">Logout</button>
        <button class="nav-button" @click.prevent="">About</button>
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
        :pid="entry.pid"
        :site="entry.site"
        :link="entry.link"
        :username="entry.username"
        :password="entry.password"
        @click.prevent="toggleCard(index)"
        @OnEditPassword="showEditModal"
        @OnDelPassword="showDeleteModal"
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
        @click.prevent="showNewModal"
      >
        <svg viewBox="0 0 20 20" enable-background="new 0 0 20 20" class="w-6 h-6 inline-block">
          <path
            fill="currentColor"
            d="M16,10c0,0.553-0.048,1-0.601,1H11v4.399C11,15.951,10.553,16,10,16c-0.553,0-1-0.049-1-0.601V11H4.601
                                    C4.049,11,4,10.553,4,10c0-0.553,0.049-1,0.601-1H9V4.601C9,4.048,9.447,4,10,4c0.553,0,1,0.048,1,0.601V9h4.399
                                    C15.952,9,16,9.447,16,10z"
          />
        </svg>
      </button>

      <password-modal
        v-model:showModal="showModal"
        :isEditorMode="isEdit"
        :pid="current.pid"
        :site="current.site"
        :link="current.link"
        :username="current.username"
        :password="current.password"
      />

      <delete-modal
        v-model:showDelModal="showDelModal"
        :pid="current.pid"
        :site="current.site"
        :link="current.link"
        :username="current.username"
        :password="current.password"
      />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { mapGetters, mapActions } from "vuex";

import Password from "../components/PasswordComponent.vue";
import PasswordModal from "../components/PasswordModalComponent.vue";
import DeleteModal from "../components/DeleteModalComponent.vue";

export default {
  name: "Home",

  components: { Password, PasswordModal, DeleteModal },

  setup() {
    const pwds = ref([]);
    return { pwds };
  },

  data() {
    return {
      isActive: null,
      searchItem: "",
      showModal: false,
      showDelModal: false,
      isEdit: false,

      current: {
        pid: "",
        site: "",
        link: "",
        username: "",
        password: "",
      },
    };
  },

  /* lifecycle hooks */
  created() {
    return this.$store.dispatch("getPasswords");
  },

  mounted() {
    document.addEventListener("click", (e) => {
      e.preventDefault();
      if (this.isActive !== null && !this.pwds[this.isActive].$el.contains(e.target)) {
        this.isActive = null;
      }
    });
  },

  /* methods */
  methods: {
    ...mapActions(["logOut"]),

    toggleCard(index) {
      this.isActive = index;
    },

    showEditModal(e) {
      this.isEdit = true;
      this.current = (({ pid, site, link, username, password }) => ({ pid, site, link, username, password }))(e);
      this.showModal = !this.showModal;
    },

    showNewModal() {
      this.current = {};
      this.isEdit = false;
      this.showModal = !this.showModal;
    },

    showDeleteModal(e) {
      this.current = (({ pid, site, link, username, password }) => ({ pid, site, link, username, password }))(e);

      this.showDelModal = !this.showDelModal;
    },

    async logoutHandler() {
      await this.logOut();
      await this.$router.push("/login");
    },
  },

  computed: {
    ...mapGetters({ entries: "statePasswords" }),
    matchSearchItem() {
      if (this.searchItem === "") {
        return this.entries;
      } else {
        return this.entries.filter((entry) => entry.site.toLowerCase().includes(this.searchItem.toLowerCase()));
      }
    },
  },
};
</script>

<style scoped lang="postcss">
.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.fade-modal-enter-from,
.fade-modal-leave-to {
  opacity: 0;
}

.nav-button {
  @apply bg-dark-secondary
          flex
          items-center
          justify-center
          rounded-full
          shadow-xl
          col-span-1
          transition
          duration-300
          ease-in-out
          transform
          hover:-translate-y-1;
}
</style>