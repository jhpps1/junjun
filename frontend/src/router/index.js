import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import CommunityPage from '../components/CommunityPage.vue'

const routes = [
  { path: '/', component: App },
  { path: '/community', component: CommunityPage }
  // ...다른 페이지
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
