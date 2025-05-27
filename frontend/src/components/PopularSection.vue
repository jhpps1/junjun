<template>
  <section class="mb-5">
    <h2 class="fw-bold mb-4">인기도서</h2>
    <div class="d-flex align-items-center">
      <button class="btn btn-outline-secondary me-2">&#8592;</button>
      <div class="flex-grow-1 d-flex justify-content-between">
        <div v-for="n in 4" :key="n" class="card mx-1 p-3 text-center" style="width: 200px;">
          <div class="mb-2">[책 아이콘]</div>
          <div>작가</div>
          <div class="fw-bold">책이름</div>
          <div>100%</div>
          <div class="small text-muted mt-2">댓글 세로 캐러셀</div>
        </div>
      </div>
      <button class="btn btn-outline-secondary ms-2">&#8594;</button>
    </div>
    <button class="btn btn-outline-dark mt-3">더보기 ...</button>
  </section>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import BookCard from '@/components/BookCard.vue'

const books = ref([])
const loading = ref(true)
const showCount = 3
const currentIdx = ref(0)

// visibleBooks: books가 비어있을 때 안전하게 처리
const visibleBooks = computed(() => {
  if (!books.value.length) return []
  const arr = []
  for (let i = 0; i < showCount; i++) {
    arr.push(books.value[(currentIdx.value + i) % books.value.length])
  }
  return arr
})

let interval = null

onMounted(async () => {
  loading.value = true
  try {
    // 1️⃣ 인기순 도서 API 호출
    const res = await axios.get('http://localhost:8000/api/books/popular/')
    // 실제 응답이 배열인지 확인하고 보정
    if (Array.isArray(res.data)) {
      books.value = res.data.map(book => ({
        ...book,
        comments: book.comments && book.comments.length ? book.comments : ['아직 댓글 없음']
      }))
    } else if (Array.isArray(res.data.results)) {
      books.value = res.data.results.map(book => ({
        ...book,
        comments: book.comments && book.comments.length ? book.comments : ['아직 댓글 없음']
      }))
    } else {
      books.value = []
    }
    // 2️⃣ 캐러셀 자동 순환
    if (books.value.length > 0) {
      interval = setInterval(() => {
        currentIdx.value = (currentIdx.value + 1) % books.value.length
      }, 2500)
    }
  } catch (err) {
    alert('인기도서 데이터를 불러올 수 없습니다.')
    books.value = []
  } finally {
    loading.value = false
  }
})

onUnmounted(() => {
  if (interval) clearInterval(interval)
})
</script>
