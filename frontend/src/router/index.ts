import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
// import RecommendView from '../views/RecommendView.vue' // 필요시 주석 해제

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  // {
  //   path: '/recommend',
  //   name: 'recommend',
  //   component: RecommendView // RecommendView를 사용한다면 주석 해제
  // },
  // 다른 라우트들을 여기에 추가할 수 있습니다.
]

const router = createRouter({
  history: createWebHistory(), // 인자 없이 호출하여 Vite가 BASE_URL을 자동으로 처리하도록 함
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    } else if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
