import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/views/HomeView.vue";
import Authorization from "@/views/Authorization.vue";
import StudentView from "@/views/StudentView.vue";
import Scheduler from "@/views/Scheduler.vue";
import StudentSubjects from "@/views/StudentSubjects.vue";
import GuarantorView from "@/views/GuarantorView.vue";
import GuarantorInstructors from "@/views/GuarantorInstructors.vue";
import GuarantorActivities from "@/views/GuarantorActivities.vue";
import StudentActivities from "@/views/StudentActivities.vue";
import Admin from "@/views/Admin.vue";
import InstructorView from "@/views/InstructorView.vue";
import InstructorActivities from "@/views/InstructorActivities.vue";

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
      component: Scheduler,
      beforeEnter: (to, from, next) => {
        const status = localStorage.getItem('status');
        if (status !== 'Scheduler') {
          next('/');
        } else {
          next();
        }
      }
    },
    {
      path: '/student/subjects',
      component: StudentSubjects,
    },
    {
      path: '/student/activities',
      component: StudentActivities,
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
      beforeEnter: (to, from, next) => {
        const status = localStorage.getItem('status');
        if (status !== 'Admin') {
          next('/');
        } else {
          next();
        }
      }
    },
    {
      path: '/instructor',
      component: InstructorView,
    },
    {
      path: '/instructor/activities',
      component: InstructorActivities,
    },

  ]
})

export default router
