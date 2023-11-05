import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import Authorization from "@/views/Authorization.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/authorization',
      component: Authorization
    }
  ]
})

export default router
