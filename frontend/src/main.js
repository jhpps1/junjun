import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
// 라우트와 스토어 가져오기
import HomeView from './views/HomeView.vue'
import { useBookStore } from './stores/book.ts'
import { useAuthStore } from './stores/auth.js'

// 라우트 설정 - '/' 경로 추가
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView  // 홈 경로에 HomeView 컴포넌트 연결
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('./views/LoginView.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('./views/RegisterView.vue')
  }
]

// 라우터 생성
const router = createRouter({
  history: createWebHistory(),
  routes,
  // 스크롤 동작 정의
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

// Pinia 인스턴스 생성
const pinia = createPinia()

// 앱 생성 및 라우터, Pinia 연결
const app = createApp(App)
app.use(router)
app.use(pinia)

// 앱이 마운트되기 전에 필요한 데이터 불러오기
const initializeApp = async () => {
  try {
    // 인증 상태 초기화 (토큰이 있으면 사용자 정보 불러오기)
    const authStore = useAuthStore()
    authStore.initializeAuth()
    
    // 책 데이터 초기화
    const bookStore = useBookStore()
    await bookStore.loadFixtureData()
    
    // 데이터 로드 후 앱 마운트
    app.mount('#app')
  } catch (error) {
    console.error("앱 초기화 중 오류 발생:", error)
    // 오류가 발생해도 앱은 마운트 (사용자 경험을 위해)
    app.mount('#app')
  }
}

// 앱 초기화 실행
initializeApp()
