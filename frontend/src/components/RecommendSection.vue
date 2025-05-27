<template>
  <section class="container py-5">
    <div class="row">
      <!-- 왼쪽: 선택된 책 크게 -->
      <div class="col-md-6 d-flex flex-column align-items-center justify-content-center border-end">
        <img
          v-if="selectedBook && selectedBook.cover"
          :src="selectedBook.cover"
          alt="Book Cover"
          class="mb-4"
          style="object-fit:contain; width:70%; max-height:340px; background:#fff; border-radius:12px;"
        />
        <h2 class="fw-bold mb-2">{{ selectedBook?.title }}</h2>
        <div class="mb-3 text-muted">{{ selectedBook?.summary }}</div>
      </div>

      <!-- 오른쪽: 추천 도서 3개 세로 -->
      <div class="col-md-6">
        <div class="d-flex flex-column gap-4">
          <div
            v-for="(book, idx) in recommendedBooks"
            :key="book.id"
            class="p-4 border rounded-3 position-relative bg-white"
            :class="{ 'border-2 border-dark': selectedBook && selectedBook.id === book.id }"
            @click="selectBook(book)"
            style="cursor:pointer;"
          >
            <div class="d-flex align-items-center mb-1">
              <h5 class="fw-bold mb-0 me-2">{{ book.title }}</h5>
              <span
                class="badge ms-2"
                :style="{ backgroundColor: (book.category && book.category.color) ? book.category.color : '#888', color: '#fff' }"
              >{{ (book.category && book.category.name) ? book.category.name : '카테고리없음' }}</span>
            </div>
            <div class="mb-2 small text-muted">
              {{ book.summary }}
            </div>
            <div class="mb-2 d-flex align-items-center gap-3">
              <button
                class="btn btn-outline-secondary btn-sm"
                @click.stop="toggleLike(book)"
              >
                <i :class="book.isLiked ? 'bi-heart-fill text-danger' : 'bi-heart'"></i> 찜하기
              </button>
              <button
                class="btn btn-outline-secondary btn-sm"
                @click.stop="toggleRead(book)"
              >
                <i :class="book.isRead ? 'bi-check-circle-fill text-primary' : 'bi-circle'"></i> 이미 읽음
              </button>
            </div>
            <button
              class="btn btn-dark btn-sm"
              @click.stop="goToDetail(book.id)"
            >
              자세히
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { fetchRecommendedBooksByColor } from '@/api/book'

const userId = 1 // 실제 로그인된 유저의 ID로 교체
const recommendedBooks = ref([])
const selectedBook = ref(null)
const router = useRouter()

onMounted(async () => {
  try {
    const { data } = await fetchRecommendedBooksByColor(userId)
    // { similar, different, random } 구조를 배열로
    recommendedBooks.value = [data.similar, data.different, data.random].filter(Boolean)
    selectedBook.value = recommendedBooks.value[0] || null
    console.log('추천도서:', recommendedBooks.value)
  } catch (error) {
    console.error('추천도서 로딩 에러:', error)
    recommendedBooks.value = []
  }
  console.log('userId', userId)
  const { data } = await fetchRecommendedBooksByColor(userId)
})

const selectBook = (book) => {
  selectedBook.value = book
}

const toggleLike = (book) => {
  book.isLiked = !book.isLiked
  // TODO: 서버에 반영할 API가 있으면 여기에 추가
}

const toggleRead = (book) => {
  book.isRead = !book.isRead
  // TODO: 서버에 반영할 API가 있으면 여기에 추가
}

const goToDetail = (bookId) => {
  router.push(`/books/${bookId}`)
}
</script>
