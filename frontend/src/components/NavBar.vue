<template>
  <nav class="navbar navbar-expand navbar-light bg-white shadow-sm px-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand fw-bold text-dark">BookPalette</router-link>
      <div class="d-flex align-items-center ms-auto">
        <template v-if="userStore.isLogin">
          <span class="fw-semibold me-3">{{ userStore.user.username }}님</span>
          <router-link to="/profile" class="btn btn-outline-primary btn-sm me-2">내 정보</router-link>
          <button @click="userStore.logout" class="btn btn-outline-secondary btn-sm">로그아웃</button>
        </template>
        <template v-else>
          <button @click="$emit('show-login')" class="btn btn-outline-primary btn-sm me-2">로그인</button>
          <button @click="$emit('show-register')" class="btn btn-dark btn-sm">회원가입</button>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useUserStore } from '../store/user'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const userStore = useUserStore()
const router = useRouter()

onMounted(() => {
  userStore.fetchMe()
})

function handleLogout() {
  userStore.logout()
  userStore.fetchMe() // 로그아웃 후 바로 상태 갱신!
  router.push('/')
  // 또는, 강제 새로고침을 원하면 window.location.reload() 사용
  // window.location.reload()
}

function scrollTo(section) {
  const el = document.getElementById(section)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
function goProfile() {
  router.push('/profile')
}
function goHome() {
  router.push('/')
}

defineEmits(['show-login', 'show-register'])
</script>

