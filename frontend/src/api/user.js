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

export const postPass = async ({ site, link, username, password }) => {
  return await axios.post("passwords/", { site, link, username, password });
};

// await axios.post("passwords/", { "site": "google", "link": "http://www.google.com", "username": "hello", "password" : "world" })
