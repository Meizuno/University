import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import Authorization from "@/views/Authorization.vue";
import StudentView from "@/views/StudentView.vue";

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
      component: Authorization,
    },
    {
      path: '/student',
      component: StudentView,
    }

  ]
})

export default router
