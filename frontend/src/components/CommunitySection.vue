
<template>
  <div class="flex flex-col gap-8 py-16 items-center">
    <div
      v-for="thread in threads"
      :key="thread.id"
      class="w-full max-w-2xl rounded-xl border px-8 py-6 bg-white shadow hover:shadow-lg transition"
    >
      <div class="flex items-center gap-3 mb-2">
        <!-- 작성자 컬러 뱃지/원형 -->
        <div class="w-8 h-8 rounded-full border-2"
             :style="{ backgroundColor: thread.user.profile_color, borderColor: thread.user.profile_color }"></div>
        <span class="font-bold">{{ thread.user.username }}</span>
        <span class="ml-auto text-xs text-gray-400">{{ formatDate(thread.created_at) }}</span>
      </div>
      <div class="text-xl font-bold mb-1">{{ thread.title }}</div>
      <div class="text-gray-700 whitespace-pre-line">{{ thread.content }}</div>
      <ThreadCommentList :threadId="thread.id" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'
import ThreadCommentList from './ThreadCommentList.vue'
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
