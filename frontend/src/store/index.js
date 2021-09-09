import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import users from "./modules/users";
import passwords from "./modules/passwords";
import SecureLS from "secure-ls";

const ls = new SecureLS({ isCompression: false });

export default createStore({
  modules: {
    users,
    passwords,
  },
  plugins: [
    createPersistedState({
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      },
    }),
  ],
});
