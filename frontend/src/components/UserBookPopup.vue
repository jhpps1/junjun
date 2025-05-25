<template>
  <div class="fixed inset-0 bg-black/30 flex items-center justify-center z-40">
    <div class="bg-white rounded-2xl p-6 shadow max-w-xl min-w-[320px] relative">
      <button @click="$emit('close')" class="absolute top-2 right-3 text-xl text-gray-400">×</button>
      <div class="flex items-center gap-3 mb-4">
        <div class="w-8 h-8 rounded-full border-2" :style="{ backgroundColor: user.profile_color }"></div>
        <span class="font-bold">{{ user.username }}</span>
        <span class="ml-3 text-xs text-gray-500">컬러: {{ user.profile_color }}</span>
      </div>
      <div class="mb-3 font-semibold">찜한 책</div>
      <ul class="mb-4">
        <li v-for="book in likedBooks" :key="book.id" class="text-sm mb-1">📚 {{ book.title }}</li>
      </ul>
      <div class="mb-3 font-semibold">읽은 책</div>
      <ul>
        <li v-for="book in readBooks" :key="book.id" class="text-sm mb-1">✔️ {{ book.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from '../axios.js'
const props = defineProps({ user: Object })
const likedBooks = ref([])
const readBooks = ref([])

watch(() => props.user, async (newUser) => {
  if (!newUser) return
  // relations/?user={id}&status=like
  const resLike = await axios.get(`/api/relations/?user=${newUser.id}&status=like`)
  likedBooks.value = resLike.data
  const resRead = await axios.get(`/api/relations/?user=${newUser.id}&status=read`)
  readBooks.value = resRead.data
}, { immediate: true })
</script>
