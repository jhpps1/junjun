<template>
  <div class="container my-4" id="popular">
    <h2 class="fw-bold mb-3">인기도서</h2>
    <div class="d-flex overflow-auto gap-3 pb-2">
      <div v-for="book in books" :key="book.id" class="card" style="min-width: 140px;">
        <img :src="book.cover" class="card-img-top" alt="..." />
        <div class="card-body p-2">
          <h6 class="card-title mb-1">{{ book.title }}</h6>
        </div>
      </div>
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
