<template>
  <div class="container d-flex flex-column justify-content-center align-items-center" style="min-height: 80vh;">
    <div class="card shadow p-4" style="max-width: 350px; width: 100%;">
      <h2 class="mb-4 text-center fw-bold">회원가입</h2>
      <form @submit.prevent="onRegister">
        <div class="mb-3">
          <label class="form-label">아이디</label>
          <input v-model="username" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">비밀번호</label>
          <input v-model="password" type="password" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">비밀번호 확인</label>
          <input v-model="password2" type="password" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-success w-100">회원가입</button>
      </form>
      <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
      <div class="mt-3 text-center">
        <router-link to="/login">이미 계정이 있으신가요? 로그인</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const username = ref('')
const password = ref('')
const password2 = ref('')
const error = ref('')
const router = useRouter()

async function onRegister() {
  error.value = ''
  if (password.value !== password2.value) {
    error.value = '비밀번호가 일치하지 않습니다.'
    return
  }
  try {
    await axios.post('http://localhost:8000/api/accounts/register/', {
      username: username.value,
      password: password.value,
    })
    alert('회원가입 성공! 로그인 해주세요.')
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.detail || '회원가입 실패'
  }
}
</script>
