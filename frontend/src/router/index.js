import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import UserProfileView from '@/views/UserProfileView.vue'

const routes = [
  { path: '/login', component: LoginView, name: 'Login' },
  { path: '/register', component: RegisterView, name: 'Register' },
  { path: '/', component: HomeView, name: 'Home' },
  { path: '/community', component: CommunityView, name: 'Community' },
  { path: '/profile', component: UserProfileView, name: 'UserProfile' },
]

export default createRouter({
  history: createWebHistory(),
  routes
})
