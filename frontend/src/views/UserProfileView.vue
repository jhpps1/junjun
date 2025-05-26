<template>
  <div class="container py-5">
    <div class="d-flex align-items-center mb-4">
      <h2 class="fw-bold mb-0">내 정보</h2>
    </div>
    <div class="card mx-auto" style="max-width: 500px;">
      <div class="card-body">
        <h4 class="mb-3 fw-bold">{{ user?.username }}</h4>
        <div class="mb-3">
          <span class="fw-semibold">내 컬러</span>
          <span
            class="badge rounded-pill ms-2"
            :style="{ background: user?.profile_color || '#ccc', color: '#fff' }"
          >
            {{ user?.profile_color || '지정안됨' }}
          </span>
        </div>
        <hr>
        <div class="mb-3">
          <span class="fw-semibold">작성한 커뮤니티 스레드</span>
          <ul class="list-group mt-2" v-if="threads.length">
            <li
              v-for="thread in threads"
              :key="thread.id"
              class="list-group-item"
            >
              {{ thread.title }}
              <small class="text-muted ms-2">({{ thread.created_at.slice(0, 10) }})</small>
            </li>
          </ul>
          <div v-else class="text-muted small">아직 작성한 스레드가 없습니다.</div>
        </div>
        <hr>
        <div class="mb-3">
          <span class="fw-semibold">좋아요 한 책</span>
          <ul class="list-group mt-2" v-if="likes.length">
            <li v-for="book in likes" :key="book.id" class="list-group-item">
              {{ book.title }} <small class="text-muted">({{ book.author }})</small>
            </li>
          </ul>
          <div v-else class="text-muted small">좋아요 한 책이 없습니다.</div>
        </div>
        <hr>
        <div class="mb-3">
          <span class="fw-semibold">읽은 책</span>
          <ul class="list-group mt-2" v-if="reads.length">
            <li v-for="book in reads" :key="book.id" class="list-group-item">
              {{ book.title }} <small class="text-muted">({{ book.author }})</small>
            </li>
          </ul>
          <div v-else class="text-muted small">아직 읽은 책이 없습니다.</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/store/user'
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

// Pinia로부터 user 정보
const userStore = useUserStore()
const user = userStore.user

const router = useRouter()
function goHome() {
  router.push('/')
}

// 임시 예시 데이터 (API 연동 필요시 onMounted 등에서 fetch!)
const threads = ref([
  { id: 1, title: '첫 번째 스레드', created_at: '2024-06-01T09:30:00' },
  { id: 2, title: '나의 독서 후기', created_at: '2024-06-05T12:10:00' },
])
const likes = ref([
  { id: 1, title: '코딩, 너의 의미', author: '작가C' },
  { id: 2, title: '달의 영휴', author: '작가A' },
])
const reads = ref([
  { id: 1, title: '마음의 과학', author: '작가B' },
])
// 실제로는 API fetch로 변경 가능
</script>
