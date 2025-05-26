<template>
  <section id="popular" class="container py-5">
    <h2 class="fw-bold">인기도서</h2>
    <p class="text-muted">금주의 인기 도서를 알아보세요</p>
    <div class="d-flex align-items-center">
      <button class="btn btn-outline-secondary me-2" @click="prev">
        <i class="bi bi-arrow-left"></i>
      </button>
      <div class="flex-grow-1">
        <div class="row row-cols-1 row-cols-md-4 g-3">
          <BookCard
            v-for="book in visibleBooks"
            :key="book.id"
            :book="book"
          />
        </div>
      </div>
      <button class="btn btn-outline-secondary ms-2" @click="next">
        <i class="bi bi-arrow-right"></i>
      </button>
    </div>
    <div class="d-flex justify-content-end mt-2">
      <button class="btn btn-dark btn-sm me-2">더보기</button>
      <button class="btn btn-outline-dark btn-sm"><i class="bi bi-three-dots"></i></button>
    </div>
  </section>
</template>
<script setup>
import { ref, computed } from 'vue'
import BookCard from '@/components/BookCard.vue'
const books = ref([
  { id: 1, title: '미움받을 용기', author: '기시미 이치로', comments: ['정말 좋아요', '추천합니다'] },
  { id: 2, title: '죽고 싶지만 떡볶이는 먹고 싶어', author: '백세희', comments: ['마음에 와닿는 책', '위로가 되었어요'] },
  { id: 3, title: '데미안', author: '헤르만 헤세', comments: ['철학적인 책', '다시 읽고 싶은 책'] },
  { id: 4, title: '자존감 수업', author: '윤홍균', comments: ['자존감 UP!', '좋은 조언이 많아요'] }
])
const start = ref(0)
const showCount = 4
const visibleBooks = computed(() => books.value.slice(start.value, start.value + showCount))
function prev() { if (start.value > 0) start.value-- }
function next() { if (start.value + showCount < books.value.length) start.value++ }
</script>
