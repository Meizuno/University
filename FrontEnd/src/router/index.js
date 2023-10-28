import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Authorization.vue'
import Authorization from "@/views/Authorization.vue";
import StudentView from "@/views/StudentView.vue";

const routes = [
  {
    path: '/',
    redirect: '/authorization',
  },
  {
    path: '/authorization',
    name: 'authorization',
    component: Authorization
  },
  {
    path: '/student',
    name: 'student',
    component: StudentView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
