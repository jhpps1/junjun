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
