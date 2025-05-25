<template>
  <div>
    <!-- 네비게이션 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm sticky-top">
      <div class="container">
        <a class="navbar-brand fw-bold text-primary" href="#">BookPalette</a>
        <div class="ms-auto d-flex gap-2 align-items-center">
          <template v-if="user">
            <span class="badge bg-primary text-light">{{ user.username }}님</span>
            <button class="btn btn-outline-primary" @click="showProfile">마이페이지</button>
            <button class="btn btn-outline-secondary" @click="logout">로그아웃</button>
          </template>
          <template v-else>
            <button class="btn btn-primary" @click="showLogin">로그인</button>
            <button class="btn btn-success" @click="showRegister">회원가입</button>
          </template>
        </div>
      </div>
    </nav>

    <!-- 본문 -->
    <div class="container py-5">
      <!-- 뷰 전환 -->
      <div v-if="currentView === 'login'">
        <LoginForm @login-success="() => { fetchMe(); showMain(); }" />
      </div>
      <div v-else-if="currentView === 'register'">
        <RegisterForm @register-success="showLogin" />
      </div>
      <div v-else-if="currentView === 'profile'">
        <ProfileSection @color-change="handleColorChange" />
      </div>

      <!-- 메인 섹션들 -->
      <main v-else>
        <HeroSection />
        <hr />
        <CategorySection />
        <hr />
        <BookRecommendSection :key="bookRecKey" />
        <hr />
        <ThreadWriteSection />
        <CommunitySection />
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from './axios'

import HeroSection from './components/HeroSection.vue'
import CategorySection from './components/CategorySection.vue'
import BookRecommendSection from './components/BookRecommendSection.vue'
import CommunitySection from './components/CommunitySection.vue'
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'
import ProfileSection from './components/ProfileSection.vue'
import ThreadWriteSection from './components/ThreadWriteSection.vue'

const user = ref(null)
const currentView = ref('main')
const bookRecKey = ref(Date.now())

onMounted(fetchMe)
async function fetchMe() {
  try {
    const res = await axios.get('/api/users/me/')
    user.value = res.data
  } catch {
    user.value = null
  }
}
function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  user.value = null
  currentView.value = 'main'
  window.location.reload()
}
function showLogin() { currentView.value = 'login' }
function showRegister() { currentView.value = 'register' }
function showProfile() { currentView.value = 'profile' }
function showMain() { currentView.value = 'main' }
function handleColorChange() {
  bookRecKey.value = Date.now()
}
</script>
