<template>
  <div
    class="modal fade show"
    tabindex="-1"
    style="display: block; background: rgba(0,0,0,0.25);"
    @click.self="$emit('close')"
  >
    <div class="modal-dialog modal-dialog-centered" style="max-width: 400px;">
      <div class="modal-content rounded-4 shadow-lg border-0">
        <div class="modal-header border-0">
          <h5 class="modal-title fw-bold">로그인</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="login">
            <div class="mb-3">
              <input v-model="username" class="form-control" placeholder="아이디" required />
            </div>
            <div class="mb-3">
              <input v-model="password" type="password" class="form-control" placeholder="비밀번호" required />
            </div>
            <button type="submit" class="btn btn-dark w-100 rounded-3 py-2 fw-bold">
              로그인
            </button>
          </form>
          <div class="d-flex justify-content-between align-items-center mt-3">
            <a href="#" class="link-primary small" @click.prevent="$emit('switch-register')">
              회원가입
            </a>
            <button class="btn btn-secondary btn-sm" @click="$emit('close')">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '../store/user'

const username = ref("")
const password = ref("")
const userStore = useUserStore()

const login = async () => {
  try {
    await userStore.login(username.value, password.value)
    // 로그인 성공 → 모달 닫기 + 네비바 등 자동 반영
    window.location.reload() // 새로고침 시 세션 상태 완벽 반영!
  } catch (error) {
    alert(error.response?.data?.detail || error.message)
  }
}
</script>
