<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top shadow-sm">
    <div class="container">
      <!-- BookPalette 로고: 클릭시 홈 이동 -->
      <a
        class="navbar-brand fw-bold"
        style="cursor:pointer"
        @click="goHome"
      >
        BookPalette
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="#popular" @click.prevent="scrollTo('popular')">인기도서</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#recommend" @click.prevent="scrollTo('recommend')">추천도서</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#category" @click.prevent="scrollTo('category')">카테고리</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#community" @click.prevent="scrollTo('community')">커뮤니티</a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <template v-if="!userStore.isLoggedIn">
            <li class="nav-item">
              <span class="nav-link" style="cursor:pointer" @click="$emit('show-login')">로그인</span>
            </li>
            <li class="nav-item">
              <span class="nav-link" style="cursor:pointer" @click="$emit('show-register')">회원가입</span>
            </li>
          </template>
          <template v-else>
            <li class="nav-item">
              <span class="nav-link" style="cursor:pointer" @click="handleLogout">로그아웃</span>
            </li>
            <li class="nav-item">
              <span class="nav-link" style="cursor:pointer" @click="goProfile">
                {{ userStore.user?.username || '내 정보' }}
              </span>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useUserStore } from '@/store/user'
import { useRouter } from 'vue-router'
const userStore = useUserStore()
const router = useRouter()

function handleLogout() {
  userStore.logout()
  // 필요시 새로고침이나 홈 이동
  router.push('/')
}
function scrollTo(section) {
  const el = document.getElementById(section)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
function goProfile() {
  router.push('/profile')
}
// ★ 로고 클릭 → 홈 이동
function goHome() {
  router.push('/')
}
defineEmits(['show-login', 'show-register'])
</script>
