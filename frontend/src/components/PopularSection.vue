<template>
  <section class="popular-section">
    <h2 class="section-title">인기도서</h2>
    <p class="section-desc">금주의 인기 도서를 알아보세요</p>
    <div class="carousel">
      <button class="arrow-btn" @click="prev">&#8592;</button>
      <div class="cards">
        <BookCard v-for="book in visibleBooks" :key="book.id" :book="book" />
      </div>
      <button class="arrow-btn" @click="next">&#8594;</button>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import BookCard from '@/components/BookCard.vue'

const books = ref([])
const currentIdx = ref(0)
const showCount = 4

const visibleBooks = computed(() => {
  const arr = []
  for (let i = 0; i < showCount; i++) {
    arr.push(books.value[(currentIdx.value + i) % books.value.length])
  }
  return arr
})

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/api/books/popular/')
  books.value = res.data
})

function prev() {
  currentIdx.value = (currentIdx.value - 1 + books.value.length) % books.value.length
}
function next() {
  currentIdx.value = (currentIdx.value + 1) % books.value.length
}
</script>

<style scoped>
.popular-section { margin: 2rem 0; }
.section-title { font-size: 2rem; font-weight: 700; }
.section-desc { font-size: 1rem; color: #333; margin-bottom: 1.2rem; }
.carousel { display: flex; align-items: center; justify-content: center; }
.cards {
  display: flex; gap: 2rem;
}
.arrow-btn {
  border: 1px solid #111;
  background: #fff;
  font-size: 1.2rem;
  width: 40px; height: 40px; border-radius: 8px;
  cursor: pointer;
  transition: background 0.1s;
}
.arrow-btn:hover { background: #f5f5f5; }
</style>
