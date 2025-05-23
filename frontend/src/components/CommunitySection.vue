<template>
  <div class="flex flex-col gap-6 py-16">
    <div
      v-for="thread in threads"
      :key="thread.id"
      class="rounded-xl border px-8 py-6 bg-white"
    >
      <div class="flex items-center gap-3 mb-2">
        <div class="w-8 h-8 rounded-full" :style="{ backgroundColor: thread.user.profile_color }"></div>
        <span class="font-bold">{{ thread.user.username }}</span>
      </div>
      <div class="text-xl font-bold">{{ thread.title }}</div>
      <div class="text-gray-700 mt-1">{{ thread.content }}</div>
      <div class="text-xs mt-2 text-gray-400">{{ thread.created_at }}</div>
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
</script>
