import { createRouter, createWebHistory } from 'vue-router'
import authorization from "@/views/Authorization.vue";
import Authorization from "@/views/Authorization.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: () => import('../views/HomeView.vue')
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
    {
      path: '/',
      redirect: '/authorization',
    },
    {
      path: '/authorization',
      component: Authorization
    }
  ]
})

export default router
