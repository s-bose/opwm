import axios from "axios";

const state = {
  passwords: null,
};

const getters = {
  statePasswords: (state) => state.passwords,
};

const actions = {
  async createPassword({ dispatch }, { site, link, username, password }) {
    await axios.post("passwords/", { site, link, username, password });
    await dispatch("getPasswords");
  },

  async getPasswords({ commit }) {
    let obj = await axios.get("passwords/all");
    commit("setPasswords", obj?.data);
  },

  async updatePassword({ dispatch }, { pid, site, link, username, password }) {
    await axios.put(`passwords/${pid}`, { site, link, username, password });
    await dispatch("getPasswords");
  },

  async deletePassword({ dispatch }, pid) {
    await axios.delete(`passwords/${pid}`);
    await dispatch("getPasswords");
  },
};

const mutations = {
  setPasswords(state, passwords) {
    state.passwords = passwords;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
