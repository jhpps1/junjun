<template>
  <section id="popular" class="container py-5 border-bottom">
    <h2 class="mb-4 fw-bold">인기도서</h2>
    <div id="popularCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div
          class="carousel-item"
          :class="{ active: idx === 0 }"
          v-for="(book, idx) in popularBooks"
          :key="book.id"
        >
          <div class="d-flex justify-content-center">
            <div class="card shadow-sm" style="width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">{{ book.title }}</h5>
                <p class="card-text">{{ book.author }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#popularCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#popularCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
      </button>
    </div>
  </section>

  <section id="recommend" class="container py-5 border-bottom">
    <h2 class="mb-4 fw-bold">추천도서</h2>
    <div id="recommendCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div
          class="carousel-item"
          :class="{ active: idx === 0 }"
          v-for="(book, idx) in recommendBooks"
          :key="book.id"
        >
          <div class="d-flex justify-content-center">
            <div class="card shadow-sm" style="width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">{{ book.title }}</h5>
                <p class="card-text">{{ book.author }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#recommendCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#recommendCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

// 샘플 데이터 (실제로는 API 등에서 받아옴)
const popularBooks = ref([
  { id: 1, title: '인기 1', author: '저자 1' },
  { id: 2, title: '인기 2', author: '저자 2' },
  { id: 3, title: '인기 3', author: '저자 3' },
  { id: 4, title: '인기 4', author: '저자 4' }
])

const recommendBooks = ref([
  { id: 1, title: '추천 1', author: '저자 A' },
  { id: 2, title: '추천 2', author: '저자 B' },
  { id: 3, title: '추천 3', author: '저자 C' }
])
</script>
