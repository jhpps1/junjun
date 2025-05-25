<!-- src/components/ThreadCommentList.vue -->
<template>
  <div class="mt-6">
    <h3 class="text-lg font-semibold mb-2">💬 댓글</h3>
    <div v-for="comment in comments" :key="comment.id" class="flex items-start gap-3 mb-4">
      <div class="w-6 h-6 rounded-full" :style="{ backgroundColor: comment.user.profile_color }"></div>
      <div class="flex-1">
        <div class="text-sm font-bold">{{ comment.user.username }}</div>
        <div class="text-sm text-gray-700 whitespace-pre-line">{{ comment.content }}</div>
        <div class="text-xs text-gray-400">{{ formatDate(comment.created_at) }}</div>
      </div>
    </div>
    <form @submit.prevent="submitComment" class="flex gap-2 mt-4">
      <input v-model="content" class="flex-1 p-2 rounded border" placeholder="댓글을 입력하세요" required />
      <button class="px-4 py-2 bg-indigo-500 text-white rounded">작성</button>
    </form>
    <p v-if="error" class="text-sm text-red-500 mt-1">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from '../axios'

const props = defineProps({ threadId: Number })
const comments = ref([])
const content = ref('')
const error = ref('')

async function fetchComments() {
  const res = await axios.get(`/api/comments/?thread=${props.threadId}`)
  comments.value = res.data
}

async function submitComment() {
  try {
    await axios.post('/api/comments/', {
      thread: props.threadId,
      content: content.value
    })
    content.value = ''
    error.value = ''
    await fetchComments()
  } catch (e) {
    error.value = e.response?.data?.detail || '작성 실패'
  }
}

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

onMounted(fetchComments)
watch(() => props.threadId, fetchComments)
</script>
