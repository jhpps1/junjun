<template>
  <section class="mb-5">
    <h2 class="fw-bold mb-4">추천 도서</h2>
    <div class="row">
      <!-- 왼쪽: 대표 추천 (이미지, 제목, 설명) -->
      <div class="col-md-4">
        <div class="border p-4 h-100 d-flex flex-column justify-content-center align-items-center">
          <div style="width:100px; height:140px; background:#eee;">책 이미지</div>
          <div class="fw-bold fs-4 mt-3">책 제목</div>
          <div class="text-muted mt-2">책 설명만</div>
        </div>
      </div>
      <!-- 오른쪽: 추천 리스트 -->
      <div class="col-md-8">
        <div v-for="n in 3" :key="n" class="border rounded p-3 mb-3">
          <div class="fw-bold">책 제목 <span class="badge bg-secondary ms-2">카테고리/색</span></div>
          <div class="small text-muted">책 간략 설명</div>
          <div class="d-flex gap-3 mt-2">
            <button class="btn btn-outline-primary btn-sm">찜하기</button>
            <button class="btn btn-outline-secondary btn-sm">이미 읽은 책</button>
            <button class="btn btn-outline-dark btn-sm ms-auto">자세히</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const recommends = ref([])       // 오른쪽 추천 3칸 데이터
const selectedBook = ref(null)   // 왼쪽에 보여줄 책

// 최초 마운트 시 백엔드 API에서 추천 데이터 받아오기
onMounted(async () => {
  try {
    const res = await axios.get('/api/books/recommend_color/?user_id=1')  // user_id 동적(로그인 연동)
    recommends.value = [
      { type: '비슷한 색', book: res.data.similar },
      { type: '가장 다른 색', book: res.data.different },
      { type: '랜덤', book: res.data.random }
    ]
    selectedBook.value = null
  } catch (err) {
    console.error('추천 API 실패:', err)
    recommends.value = []
    selectedBook.value = null
  }
})

// 오른쪽 추천 카드 클릭 시 왼쪽에 정보 표시
function selectBook(idx) {
  selectedBook.value = recommends.value[idx].book
}
</script>