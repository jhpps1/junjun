<template>
  <section id="popular" class="container py-5 border-bottom">
    <h2 class="mb-4 fw-bold">인기도서</h2>

    <!-- 1. 로딩 중 -->
    <div v-if="loading" class="text-center my-5">로딩중...</div>
    <!-- 2. 데이터 없음 -->
    <div v-else-if="books.length === 0" class="text-center my-5 text-secondary">
      인기도서 데이터가 없습니다.
    </div>
    <!-- 3. 정상 데이터 -->
    <div v-else class="position-relative">
      <div class="d-flex overflow-hidden" style="height: 240px;">
        <div
          class="d-flex transition"
          :style="{
            transform: `translateX(-${currentIdx * (100 / showCount)}%)`,
            transition: 'transform 0.6s cubic-bezier(.6,.18,.38,.96)'
          }"
          style="min-width:100%;"
        >
          <div
            v-for="(book, idx) in visibleBooks"
            :key="book?.id || idx"
            class="flex-shrink-0 px-2"
            style="width: 260px; min-width:260px;"
          >
            <BookCard v-if="book" :book="book" />
          </div>
        </div>
      </div>
    </div>
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
