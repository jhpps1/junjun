<template>
  <form @submit.prevent="submitThread" class="bg-white p-8 rounded-xl shadow max-w-lg mx-auto my-8 flex flex-col gap-4">
    <input v-model="title" placeholder="제목을 입력하세요" class="p-3 rounded border" required />
    <textarea v-model="content" placeholder="내용을 입력하세요" class="p-3 rounded border min-h-[120px]" required />
    <button type="submit" class="px-6 py-2 bg-indigo-500 text-white font-bold rounded">글쓰기</button>
    <div v-if="success" class="text-green-500 mt-2">작성 완료!</div>
    <div v-if="error" class="text-red-500 mt-2">{{ error }}</div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const title = ref('')
const content = ref('')
const success = ref(false)
const error = ref('')

async function submitThread() {
  try {
    await axios.post('/api/threads/', { title: title.value, content: content.value })
    success.value = true
    error.value = ''
    title.value = ''
    content.value = ''
    // 필요하면 새 글 목록 불러오는 로직 추가
  } catch (err) {
    error.value = err.response?.data?.detail || '에러가 발생했습니다.'
    success.value = false
  }
}
</script>
