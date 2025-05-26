<template>
  <NavBar
    @show-login="showLogin = true"
    @show-register="showRegister = true"
  />
  <router-view />    <!-- 홈/내정보/커뮤니티 등은 라우터에서 관리 -->

  <!-- 로그인/회원가입 모달 -->
  <LoginModal v-if="showLogin" @close="showLogin = false" @switch-register="switchToRegister" />
  <RegisterModal v-if="showRegister" @close="showRegister = false" @switch-login="switchToLogin" />
</template>

<style>
/* 1. html, body, #app 전체 높이 설정 */
html, body, #app {
  min-height: 100vh;
  height: 100%;
  margin: 0;
  padding: 0;
}

/* 2. body에 배경 이미지 적용 (cover/center/fixed) */
body {
  background-image: url('/bg.png');
  background-size: 80%;
  background-position: center 70px;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
@media (max-width: 900px) {
  body {
    background-size: 120%;
    background-position: center 40px;
  }
}
@media (max-width: 600px) {
  body {
    background-size: 180%;
    background-position: center 10px;
  }
}

/* 선택: App.vue의 #app에도 추가로 적용해도 무방 */
#app {
  min-height: 100vh;
}
</style>

<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'
import HomeView from './views/HomeView.vue'
import LoginModal from './components/LoginModal.vue'
import RegisterModal from './components/RegisterModal.vue'

const showLogin = ref(false)
const showRegister = ref(false)
function switchToRegister() {
  showLogin.value = false
  showRegister.value = true
}
function switchToLogin() {
  showRegister.value = false
  showLogin.value = true
}
</script>
