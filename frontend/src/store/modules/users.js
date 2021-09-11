import axios from "axios";

export const namespaced = true;

const state = {
  user: null,
};

const getters = {
  isAuthenticated: (state) => !!state.user,
  stateUser: (state) => state.user,
};

const actions = {

  async logIn({ dispatch }, { email, master_pwd }) {
    await axios.post("login", { email, master_pwd });
    await dispatch("viewMe");
  },

  async viewMe({ commit }) {
    try {
      let obj = await axios.get("user");
      commit("setUser", obj?.data);
    } catch (error) {
      console.error(error);
    }
  },
 
  async logOut({ commit }) {
    let user = null;
    commit("setPasswords", null, {root: true});
    commit("logout", user);
  },

  async deleteUser({ commit }) {
    await axios.delete("user");
    let user = null;
    commit("logout", user);
  }
  
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  logout(state, user) {
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
