<template>
  <form @submit.prevent="login" class="flex flex-col gap-4 p-8 bg-white rounded-xl shadow max-w-sm mx-auto mt-20">
    <input v-model="username" placeholder="아이디" class="p-2 rounded border" required />
    <input v-model="password" type="password" placeholder="비밀번호" class="p-2 rounded border" required />
    <button type="submit" class="px-6 py-2 bg-indigo-500 text-white font-bold rounded">로그인</button>
    <div v-if="error" class="text-red-500">{{ error }}</div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from '../axios.js'

const username = ref('')
const password = ref('')
const error = ref('')

async function login() {
  try {
    const res = await axios.post('/api/token/', { username: username.value, password: password.value })
    // JWT access/refresh 토큰 저장 (localStorage/sessionStorage)
    localStorage.setItem('access', res.data.access)
    localStorage.setItem('refresh', res.data.refresh)
    error.value = ''
    // 로그인 성공 후 원하는 곳으로 라우팅/새로고침
    window.location.reload()
  } catch (err) {
    error.value = '로그인 실패: 아이디 또는 비밀번호를 확인하세요.'
  }
}
</script>
