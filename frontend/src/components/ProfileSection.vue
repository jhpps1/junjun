<template>
  <div class="max-w-lg mx-auto my-16 p-8 rounded-2xl shadow-lg bg-white flex flex-col items-center gap-6">
    <h2 class="text-2xl font-bold mb-2">마이페이지 / 내 프로필</h2>
    <div class="flex items-center gap-4">
      <div class="w-16 h-16 rounded-full border-4" :style="{ backgroundColor: profileColor }"></div>
      <div>
        <div class="font-bold text-xl mb-1">{{ user?.username }}</div>
        <div class="text-gray-500">{{ user?.email }}</div>
      </div>
    </div>
    <div class="flex flex-col items-center gap-2 mt-4">
      <label class="font-semibold">프로필 컬러 바꾸기</label>
      <input v-model="profileColor" type="color" class="w-16 h-10 border rounded cursor-pointer" />
      <button
        @click="save"
        class="mt-2 px-4 py-2 bg-indigo-500 text-white rounded font-bold hover:bg-indigo-600"
      >저장</button>
      <span v-if="success" class="text-green-500 mt-2">변경 완료!</span>
      <span v-if="error" class="text-red-500 mt-2">{{ error }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'

const user = ref(null)
const profileColor = ref('#cccccc')
const success = ref(false)
const error = ref('')

async function fetchUser() {
  try {
    const res = await axios.get('/api/users/me/')
    user.value = res.data
    profileColor.value = res.data.profile_color || '#cccccc'
  } catch {
    user.value = null
  }
}
onMounted(fetchUser)

async function save() {
  try {
    await axios.put('/api/users/me/', { profile_color: profileColor.value })
    success.value = true
    error.value = ''
    await fetchUser()
  } catch (err) {
    success.value = false
    error.value = err.response?.data?.detail || '저장 실패'
  }
}
</script>
