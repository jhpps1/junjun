<template>
  <div v-for="thread in threads" :key="thread.id" class="mb-4 p-4 border rounded">
    <UserBadge :user="thread.user" />
    <div class="text-xl font-bold">{{ thread.title }}</div>
    <div class="text-gray-600">{{ thread.content }}</div>
    <div class="text-xs mt-2 text-gray-400">{{ thread.created_at }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import UserBadge from './UserBadge.vue'

const threads = ref([])

onMounted(async () => {
  const res = await axios.get('/api/threads/')
  threads.value = res.data.results ?? res.data
})
</script>
