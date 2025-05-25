<template>
  <div class="container my-4" id="community">
    <h2 class="fw-bold mb-3">커뮤니티</h2>
    <div class="list-group">
      <div
        v-for="thread in threads"
        :key="thread.id"
        class="list-group-item d-flex align-items-center"
      >
        <!-- 작성자 아바타 -->
        <div class="w-8 h-8 rounded-full border-2 me-3"
             :style="{ backgroundColor: thread.user.profile_color, borderColor: thread.user.profile_color }"></div>
        <div class="flex-grow-1">
          <div class="fw-bold">{{ thread.user.username }}</div>
          <div class="text-gray-700 whitespace-pre-line">{{ thread.content }}</div>
        </div>
        <button class="btn btn-outline-danger btn-sm ms-2"><i class="bi bi-heart"></i></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'
const threads = ref([])

onMounted(async () => {
  const res = await axios.get('/api/threads/')
  threads.value = res.data.results ?? res.data
})

function formatDate(dateString) {
  if (!dateString) return ''
  return new Date(dateString).toLocaleString('ko-KR', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
