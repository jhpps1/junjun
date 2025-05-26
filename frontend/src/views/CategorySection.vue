<template>
  <section id="category" class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <div>
        <h2 class="fw-bold mb-0">카테고리</h2>
        <span class="text-muted">카테고리 별 도서를 알아보세요</span>
      </div>
      <button class="btn btn-dark">전체 카테고리 보기</button>
    </div>
    <div class="d-flex align-items-center">
      <button class="btn btn-outline-secondary me-2" @click="prev">
        <i class="bi bi-arrow-left"></i>
      </button>
      <div class="flex-grow-1">
        <div class="row row-cols-1 row-cols-md-4 g-3">
          <CategoryCard v-for="cat in visibleCategories" :key="cat.id" :category="cat" />
        </div>
      </div>
      <button class="btn btn-outline-secondary ms-2" @click="next">
        <i class="bi bi-arrow-right"></i>
      </button>
    </div>
  </section>
</template>
<script setup>
import { ref, computed } from 'vue'
import CategoryCard from '@/components/CategoryCard.vue'

const categories = ref([
  { id: 1, name: '에세이', value: '에세이', color: '#a3c1da' },
  { id: 2, name: '심리', value: '심리', color: '#f8b195' },
  { id: 3, name: 'IT', value: 'IT', color: '#6dcff6' },
  { id: 4, name: '자기계발', value: '자기계발', color: '#f9d390' },
  { id: 5, name: '소설', value: '소설', color: '#c5c6c7' }
])
const start = ref(0)
const showCount = 4
const visibleCategories = computed(() => categories.value.slice(start.value, start.value + showCount))
function prev() { if (start.value > 0) start.value-- }
function next() { if (start.value + showCount < categories.value.length) start.value++ }
</script>
