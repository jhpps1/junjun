<template>
  <section class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="fw-bold mb-0">인기 도서</h2>
      <span class="fs-5 text-success fw-bold">+100%</span>
    </div>
    <div id="popularBooksCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div 
          class="carousel-item"
          :class="{ active: idx === 0 }"
          v-for="(slide, idx) in slideChunks"
          :key="idx"
        >
          <div class="row g-3">
            <div 
              class="col-md-3" 
              v-for="book in slide"
              :key="book.id"
            >
              <!-- Book 카드 시작 -->
              <div class="card shadow-sm h-100 border border-2 border-dark">
                <div class="card-body pb-0">
                  <h5 class="card-title fw-bold">{{ book.title }}</h5>
                  <h6 class="card-subtitle mb-2 text-muted">{{ book.author }}</h6>
                  <p class="card-text small text-truncate">{{ book.description }}</p>
                </div>
                <!-- 선(구분선) -->
                <hr class="m-0 border-2 border-dark" />
                <div class="card-footer bg-white border-top-0 pt-2 pb-2">
                  <div class="d-flex justify-content-between align-items-center">
                    <span class="small">댓글 {{ book.comments_count ?? 0 }}</span>
                    <span class="small text-secondary">평점 {{ book.rating ?? '-' }}</span>
                  </div>
                </div>
              </div>
              <!-- Book 카드 끝 -->
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#popularBooksCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#popularBooksCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
// fetchPopularBooks 함수는 기존 api.js 또는 axios 파일에서 import
import { fetchPopularBooks } from '@/api/api' // 실제 경로에 맞게 수정

const books = ref([])

onMounted(async () => {
  const { data } = await fetchPopularBooks()
  books.value = data
})

// 4개씩 슬라이드로 묶는 함수
const slideChunks = computed(() => {
  const chunkSize = 4
  const chunks = []
  for(let i = 0; i < books.value.length; i += chunkSize) {
    chunks.push(books.value.slice(i, i + chunkSize))
  }
  return chunks
})
</script>
