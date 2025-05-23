<template>
  <div class="flex flex-wrap gap-6 justify-center py-16">
    <div
      v-for="book in books"
      :key="book.id"
      class="w-64 p-5 rounded-xl border-2 shadow relative"
      :style="{ borderColor: book.color }"
    >
      <div class="font-bold text-lg mb-1">{{ book.title }}</div>
      <div class="mb-2">{{ book.author }}</div>
      <span class="px-2 py-1 rounded bg-white/70 text-xs" :style="{ color: book.color }">
        {{ book.category?.name }}
      </span>
      <!-- 찜 버튼 -->
      <button
        class="absolute top-2 right-2 text-2xl"
        :style="{ color: book.isLiked ? book.color : '#bbb' }"
        @click="toggleLike(book)"
      >★</button>
      <!-- 읽음 버튼 -->
      <button
        class="absolute bottom-2 right-2 text-sm"
        :style="{ color: book.isRead ? book.color : '#bbb' }"
        @click="toggleRead(book)"
      >읽음</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const books = ref([])
// relations: [{id, book, status}] 형태로 저장
const likes = ref([]) // 찜한 book id 목록
const reads = ref([]) // 읽은 book id 목록

async function fetchBooksAndRelations() {
  // 1. 책 데이터
  const resBooks = await axios.get('/api/books/')
  books.value = resBooks.data.results ?? resBooks.data

  // 2. 내 찜, 읽음 데이터
  const resLikes = await axios.get('/api/relations/?status=like')
  likes.value = resLikes.data.map(rel => rel.book)
  const resReads = await axios.get('/api/relations/?status=read')
  reads.value = resReads.data.map(rel => rel.book)

  // 3. books에 상태값 isLiked, isRead 부여
  for (const book of books.value) {
    book.isLiked = likes.value.includes(book.id)
    book.isRead = reads.value.includes(book.id)
  }
}

onMounted(fetchBooksAndRelations)

// relations 관리 (id까지 저장하고 있으면 더 효율)
async function toggleLike(book) {
  if (book.isLiked) {
    // relations에서 찜 relation의 id를 찾아서 DELETE
    const res = await axios.get('/api/relations/?status=like')
    const rel = res.data.find(r => r.book === book.id)
    if (rel) await axios.delete(`/api/relations/${rel.id}/`)
  } else {
    await axios.post('/api/relations/', { book: book.id, status: 'like' })
  }
  await fetchBooksAndRelations()
}

async function toggleRead(book) {
  if (book.isRead) {
    const res = await axios.get('/api/relations/?status=read')
    const rel = res.data.find(r => r.book === book.id)
    if (rel) await axios.delete(`/api/relations/${rel.id}/`)
  } else {
    await axios.post('/api/relations/', { book: book.id, status: 'read' })
  }
  await fetchBooksAndRelations()
}
</script>
