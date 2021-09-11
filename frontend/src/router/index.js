import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue"; // login
import Signup from "../views/Signup.vue"; // signup
import Home from "../views/Home.vue"; // home / dashboard
import Root from "../views/Root.vue"; // root ("/")

import store from "@/store"; // store

const routes = [
  {
    path: "/",
    name: "root",
    component: Root,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    meta: { requiresAuth: true },
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/About.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/reset",
    name: "Reset password",
    component: () => import( "../views/ResetPassword.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
