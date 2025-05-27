import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import TestBestseller from '@/components/test_bestseller.vue'

const routes = [
  { path: '/', component: HomeView, name: 'Home' },
  { path: '/community', component: CommunityView, name: 'Community' },
  { path: '/profile', component: UserProfileView, name: 'UserProfile' },
  { path: '/test-bestseller', component: TestBestseller, name: 'TestBestseller' },
]

export default createRouter({
  history: createWebHistory(),
  routes
})
