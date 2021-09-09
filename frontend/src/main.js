import { createApp } from "vue";
import axios from "axios";
import store from "./store";
import App from "./App.vue";
import router from "./router";

// eslint-disable-next-line no-unused-vars
import * as user from "./api/user";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api/";

import "./assets/tailwind.css";

const app = createApp(App);
app.use(store);
app.use(router).mount("#app");

window.user = user;
window.store = store;

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch("logOut");
      router.push("/login");
    } else {
      return Promise.reject(error);
    }
  }
});
