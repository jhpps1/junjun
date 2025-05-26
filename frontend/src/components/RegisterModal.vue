<template>
  <div class="modal-backdrop show" style="z-index: 1040;"></div>
  <div class="modal d-block" tabindex="-1" style="z-index: 1050;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">회원가입</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>
        <div class="modal-body">
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
        </div>
        <div class="modal-footer justify-content-between">
          <button class="btn btn-link" @click="$emit('switch-login')">로그인</button>
          <button class="btn btn-secondary" @click="$emit('close')">닫기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const password2 = ref('')
const error = ref('')

const emit = defineEmits(['close', 'switch-login'])

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
    }, { withCredentials: true }) // 쿠키 전송 허용
    error.value = ''           // ✅ 에러 메시지 꼭 초기화
    alert('회원가입 성공! 로그인 해주세요.')
    // 폼 입력값 초기화(선택)
    username.value = ''
    password.value = ''
    password2.value = ''
    // 로그인 모달로 전환
    emit('switch-login')
  } catch (err) {
    error.value = err.response?.data?.detail || '회원가입 실패'
  }
}
</script>
