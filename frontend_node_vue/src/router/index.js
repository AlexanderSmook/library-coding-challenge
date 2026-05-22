
import {createRouter, createWebHistory} from 'vue-router'
import LandingPage from "@/components/landing-page.vue";
import NewBook from "@/components/new-book.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage,
    },
    {
      path: '/new',
      name: 'new',
      component: NewBook,
    },
  ],
})

export default router