import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import Authorization from "@/views/Authorization.vue";
import StudentView from "@/views/StudentView.vue";
import Scheduler from "@/views/Scheduler.vue";
import StudentSubjects from "@/views/StudentSubjects.vue";
import GuarantorView from "@/views/GuarantorView.vue";
import GuarantorInstructors from "@/views/GuarantorInstructors.vue";
import GuarantorActivities from "@/views/GuarantorActivities.vue";
import Admin from "@/views/Admin.vue";

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
    },
    {
      path: '/scheduler',
      component: Scheduler
    },
    {
      path: '/student/subjects',
      component: StudentSubjects,
    },
    {
      path: '/guarantor',
      component: GuarantorView,
    },
    {
      path: '/guarantor/instructors',
      component: GuarantorInstructors,
    },
    {
      path: '/guarantor/activities',
      component: GuarantorActivities,
    },
    {
      path: '/admin',
      component: Admin,
    },

  ]
})

export default router
