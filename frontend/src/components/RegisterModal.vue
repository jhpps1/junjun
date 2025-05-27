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
          <h5 class="modal-title fw-bold">회원가입</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="register">
            <div class="mb-3">
              <input v-model="username" class="form-control" placeholder="아이디" required />
            </div>
            <div class="mb-3">
              <input v-model="password" type="password" class="form-control" placeholder="비밀번호" required />
            </div>
            <div class="mb-3">
              <label class="form-label">관심 카테고리 (3개 선택)</label>
              <select v-model="favoriteCategories" class="form-select" multiple required>
                <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                  {{ cat.name }}
                </option>
              </select>
              <div class="form-text">3개만 선택해야 합니다.</div>
            </div>
            <button type="submit" class="btn btn-dark w-100 rounded-3 py-2 fw-bold">
              회원가입
            </button>
          </form>
          <div class="d-flex justify-content-end align-items-center mt-3">
            <button class="btn btn-secondary btn-sm" @click="$emit('close')">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/auth'

const username = ref("")
const password = ref("")
const favoriteCategories = ref([])
const categories = ref([])

onMounted(async () => {
  const res = await api.get('/categories/')
  categories.value = res.data
})

const register = async () => {
  if (favoriteCategories.value.length !== 3) {
    alert("카테고리 3개만 선택하세요!")
    return
  }
  try {
    await api.post('/accounts/register/', {
      username: username.value,
      password: password.value,
      favorite_categories: favoriteCategories.value
    })
    alert("회원가입 완료!")
    window.location.reload()
  } catch (error) {
    alert(error.response?.data?.detail || error.message)
  }
}
</script>
