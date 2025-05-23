<template>
  <div class="grid grid-cols-2 gap-4">
    <div
      v-for="book in books"
      :key="book.id"
      class="p-4 rounded-2xl shadow flex flex-col"
      :style="{ borderLeft: `10px solid ${book.color}` }"
    >
      <div class="font-bold text-lg">{{ book.title }}</div>
      <div class="text-xs mb-2">{{ book.author }}</div>
      <span class="px-2 py-1 rounded bg-gray-100 text-xs" :style="{ color: book.color }">
        {{ book.category?.name }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'

const books = ref([])

onMounted(async () => {
  const res = await axios.get('/api/books/')
  books.value = res.data.results ?? res.data  // pagination 켜져있으면 .results
})
</script>
