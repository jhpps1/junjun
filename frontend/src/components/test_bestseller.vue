<template>  <div class="bestsellers container mx-auto px-4 py-6">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-bold">베스트셀러</h2>
      <div class="flex gap-1">
        <button 
          @click="prevSlide" 
          class="p-1.5 rounded-full hover:bg-gray-100 text-sm"
          :disabled="loading || error"
        >
          ◀
        </button>
        <button 
          @click="nextSlide" 
          class="p-1.5 rounded-full hover:bg-gray-100 text-sm"
          :disabled="loading || error"
        >
          ▶
        </button>
      </div>
    </div>

    <div v-if="loading" class="loading">
      Loading...
    </div>
    <div v-else-if="error" class="error text-red-500">
      {{ error }}
    </div>
    <div v-else class="relative overflow-hidden">
      <div 
        class="flex transition-transform duration-500 ease-in-out"
        :style="{ transform: `translateX(-${currentIndex * (100/visibleCount)}%)` }"
      >
        <div 
          v-for="book in displayBooks" 
          :key="book.isbn13"
          :class="[
            'flex-shrink-0',
            `w-[${100/visibleCount}%]`,
            'px-2'
          ]"
        >
          <TestBookCard 
            :book="book"
            class="transition-all duration-300 ease-in-out hover:-translate-y-1"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import TestBookCard from './test_BookCard.vue'
import bestsellers from '@/assets/data/bestsellers_30.json'

const books = ref([])
const loading = ref(true)
const error = ref(null)
const currentIndex = ref(0)
const visibleCount = 5 // 한 번에 보여질 도서 수
const autoSlideInterval = ref(null)

// 표시할 책들 계산
const displayBooks = computed(() => {
  if (!books.value.length) return []
  // 순환 구조를 만들기 위해 배열 복사 및 확장
  const extendedBooks = [...books.value, ...books.value]
  return extendedBooks.slice(currentIndex.value, currentIndex.value + visibleCount)
})

const nextSlide = () => {
  if (currentIndex.value >= books.value.length - 1) {
    currentIndex.value = 0
  } else {
    currentIndex.value++
  }
}

const prevSlide = () => {
  if (currentIndex.value <= 0) {
    currentIndex.value = books.value.length - 1
  } else {
    currentIndex.value--
  }
}

const startAutoSlide = () => {
  autoSlideInterval.value = setInterval(() => {
    nextSlide()
  }, 3000) // 3초마다 슬라이드
}

const stopAutoSlide = () => {
  if (autoSlideInterval.value) {
    clearInterval(autoSlideInterval.value)
  }
}

onMounted(() => {
  try {
    books.value = bestsellers
    console.log('Loaded bestsellers:', books.value)
    startAutoSlide()
  } catch (err) {
    error.value = err.message
    console.error('Error loading bestsellers:', err)
  } finally {
    loading.value = false
  }
})

onUnmounted(() => {
  stopAutoSlide()
})
</script>

<style scoped>
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 150px;
  font-size: 1rem;
  color: rgb(75, 85, 99);
}

.error {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 150px;
  font-size: 1rem;
}
</style>