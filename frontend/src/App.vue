<script setup>
import { ref, onMounted } from 'vue'
import axios from './axios'
import NavBar from './components/NavBar.vue'
import CategorySection from './components/CategorySection.vue'
import BookRecommendSection from './components/BookRecommendSection.vue'
import CommunitySection from './components/CommunitySection.vue'
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'
import HeroSection from './components/HeroSection.vue'
import ThreadWriteSection from './components/ThreadWriteSection.vue'
import ProfileSection from './components/ProfileSection.vue' 

const user = ref(null)
const currentView = ref('main') // 'main', 'login', 'register', 'profile'

async function fetchMe() {
  try {
    const res = await axios.get('/api/users/me/')
    user.value = res.data
  } catch {
    user.value = null
  }
}
onMounted(fetchMe)

function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  user.value = null
  currentView.value = 'main'
  window.location.reload()
}

function showLogin() {
  currentView.value = 'login'
}
function showRegister() {
  currentView.value = 'register'
}
function showMain() {
  currentView.value = 'main'
}
function showProfile() {
  currentView.value = 'profile'
}
function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: "smooth", block: "start" })
}
</script>

<template>
  <NavBar />

  <HeroSection @scrollTo="scrollToSection" />

  <!-- 로그인/회원가입/상태관리 상단바 -->
  <div class="flex justify-end p-4 gap-4 bg-gray-100">
    <template v-if="user">
      <span>{{ user.username }}님</span>
      <button @click="showProfile" class="px-3 py-1 bg-indigo-300 text-white rounded">마이페이지</button>
      <button @click="logout" class="px-3 py-1 bg-gray-400 text-white rounded">로그아웃</button>
    </template>
    <template v-else>
      <button @click="showLogin" class="px-3 py-1 bg-indigo-500 text-white rounded">로그인</button>
      <button @click="showRegister" class="px-3 py-1 bg-emerald-500 text-white rounded">회원가입</button>
    </template>
    <button v-if="currentView !== 'main'" @click="showMain" class="px-3 py-1 ml-4 bg-gray-200 rounded">← 돌아가기</button>
  </div>

  <!-- 뷰 전환: 로그인/회원가입/마이페이지 -->
  <div v-if="currentView === 'login'">
    <LoginForm @login-success="() => { fetchMe(); showMain(); }" />
  </div>
  <div v-else-if="currentView === 'register'">
    <RegisterForm @register-success="showLogin" />
  </div>
  <div v-else-if="currentView === 'profile'">
    <!-- 프로필 컬러 변경시 color-change 이벤트를 받아서 처리 -->
    <ProfileSection @color-change="handleColorChange" />
  </div>

  <!-- 메인(슬라이드/섹션) -->
  <main v-else class="pt-20">
    <section id="section-1" class="min-h-[80vh] flex flex-col items-center justify-center bg-gray-100">
      <h1 class="text-3xl font-bold mb-8">1. 서비스 소개</h1>
      <!-- 소개 내용 등 -->
    </section>
    <section id="section-2" class="min-h-[80vh] bg-[#E3F6F5]">
      <h1 class="text-3xl font-bold text-center py-10">2. 카테고리 색상 시각화</h1>
      <CategorySection />
    </section>
    <section id="section-3" class="min-h-[80vh] bg-[#F9F5FF]">
      <h1 class="text-3xl font-bold text-center py-10">3. 추천도서 영역</h1>
      <!--키 바뀌면 새로 렌더댐-->
      <BookRecommendSection :key="bookRecKey"/>
    </section>
    <section id="section-4" class="min-h-[80vh] bg-[#FFF7F0]">
      <h1 class="text-3xl font-bold text-center py-10">4. 커뮤니티</h1>
      <ThreadWriteSection />
      <CommunitySection />
    </section>
    <!-- ...필요시 추가 -->
  </main>
</template>
