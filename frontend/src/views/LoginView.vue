<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/store/user'

const username = ref('')
const password = ref('')
const userStore = useUserStore()
const router = useRouter()

async function onLogin() {
  await userStore.login(username.value, password.value)
  if (userStore.isLoggedIn) {
    router.push('/')
  }
}
</script>

<template>
  <div class="container d-flex flex-column justify-content-center align-items-center" style="min-height: 80vh;">
    <div class="card shadow p-4" style="max-width: 350px; width: 100%;">
      <h2 class="mb-4 text-center fw-bold">로그인</h2>
      <form @submit.prevent="onLogin">
        <div class="mb-3">
          <label class="form-label">아이디</label>
          <input v-model="username" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">비밀번호</label>
          <input v-model="password" type="password" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary w-100">로그인</button>
      </form>
      <div v-if="userStore.error" class="alert alert-danger mt-3">{{ userStore.error }}</div>
      <div class="mt-3 text-center">
        <router-link to="/register">회원가입</router-link>
      </div>
    </div>
  </div>
</template>