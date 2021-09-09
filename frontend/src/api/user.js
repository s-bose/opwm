import axios from "axios";

export const getUser = async () => {
  return await axios.get("user");
};

export const registerUser = async ({ email, master_pwd }) => {
  return await axios.post("register", { email, master_pwd });
};

export const loginUser = async ({ email, master_pwd }) => {
  return axios.post("login", { email, master_pwd });
};

export const modifyPass = async ({ pid, site, link, username, password }) => {
  return await axios.put(`passwords/${pid}`, { site, link, username, password });
};
