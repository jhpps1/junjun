<template>
  <form @submit.prevent="register" class="flex flex-col gap-4 p-8 bg-white rounded-xl shadow max-w-sm mx-auto mt-20">
    <input v-model="username" placeholder="아이디" class="p-2 rounded border" required />
    <input v-model="email" type="email" placeholder="이메일" class="p-2 rounded border" required />
    <input v-model="password" type="password" placeholder="비밀번호" class="p-2 rounded border" required />
    <button type="submit" class="px-6 py-2 bg-emerald-500 text-white font-bold rounded">회원가입</button>
    <div v-if="error" class="text-red-500">{{ error }}</div>
    <div v-if="success" class="text-green-500">{{ success }}</div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from '../axios.js'

const username = ref('')
const email = ref('')
const password = ref('')
const error = ref('')
const success = ref('')

async function register() {
  try {
    await axios.post('/api/users/', { username: username.value, email: email.value, password: password.value })
    success.value = '회원가입이 완료되었습니다! 로그인 해주세요.'
    error.value = ''
  } catch (err) {
    error.value = err.response?.data?.detail || '회원가입 실패'
    success.value = ''
  }
}
</script>
