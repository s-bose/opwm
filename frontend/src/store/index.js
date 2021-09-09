import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import users from "./modules/users";
// import SecureLS from "secure-ls";

// const ls = new SecureLS({ isCompression: false });

export default createStore({
  modules: {
    users,
    // passwords,
  },
  plugins: [createPersistedState()],
});
