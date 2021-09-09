import axios from "axios";

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
      // let { data } = await axios.get("user");
      // await commit("setUser", data);
      let obj = await axios.get("user");
      await commit("setUser", obj?.data);
    } catch (error) {
      console.error(error);
    }
  },
  //   // eslint-disable-next-line no-empty-pattern
  //   async deleteUser({}, id) {
  //     await axios.delete(`user/${id}`);
  //   },
  async logOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
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
