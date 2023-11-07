import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import Authorization from "@/views/Authorization.vue";
import Scheduler from "@/views/Scheduler.vue";

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
    },
    {
      path: '/scheduler',
      component: Scheduler
    }
  ]
})

export default router
