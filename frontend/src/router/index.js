import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";

import Home from "../views/Home.vue";
import Test from "../views/Test.vue";
import Root from "../views/Root.vue";
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
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/test",
    name: "Test",
    component: Test,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
