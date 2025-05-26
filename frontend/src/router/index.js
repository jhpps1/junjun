import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import UserProfileView from '@/views/UserProfileView.vue'

const routes = [
  { path: '/', component: HomeView, name: 'Home' },
  { path: '/community', component: CommunityView, name: 'Community' },
  { path: '/profile', component: UserProfileView, name: 'UserProfile' },
]

export default createRouter({
  history: createWebHistory(),
  routes
})
