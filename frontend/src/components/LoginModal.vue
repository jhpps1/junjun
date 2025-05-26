<template>
  <div class="modal-backdrop show" style="z-index: 1040;"></div>
  <div class="modal d-block" tabindex="-1" style="z-index: 1050;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">로그인</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>
        <div class="modal-body">
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
          <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
        </div>
        <div class="modal-footer justify-content-between">
          <button class="btn btn-link" @click="$emit('switch-register')">회원가입</button>
          <button class="btn btn-secondary" @click="$emit('close')">닫기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/store/user'
const username = ref('')
const password = ref('')
const error = ref('')
const userStore = useUserStore()

const emit = defineEmits(['close', 'switch-register'])

async function onLogin() {
  await userStore.login(username.value, password.value)
  if (userStore.isLoggedIn) {
    error.value = ''
    emit('close')    
  } else {
    error.value = userStore.error
  }
}
</script>
