import { createRouter, createWebHistory } from "vue-router";
import authentications from "./authentications";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...authentications,
    {
      path: "/",
    },
    {
      path: "/login",
      component: () => import("../views/authentications/Login.vue"),
    },
    {
      path: "/register",
      component: () => import("../views/authentications/Register.vue"),
    },
    {
      path: "/forbidden",
      name: "forbidden",
      component: () => import("../views/errors/403.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: () => import("../views/errors/404.vue"),
    },
    
  ],
});

export default router;