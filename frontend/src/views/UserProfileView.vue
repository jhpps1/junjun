<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/auth'

const user = ref({})
onMounted(async () => {
  const res = await api.get('/accounts/users/me/')
  user.value = res.data
})
</script>

<template>
  <div class="container py-5 d-flex justify-content-center">
    <div class="card shadow rounded-4 p-4" style="max-width: 500px; width: 100%;">
      <div class="d-flex align-items-center mb-3">
        <div
          class="rounded-circle me-3 flex-shrink-0"
          :style="{
            width: '48px',
            height: '48px',
            background: user.profile_color || '#ccc',
            border: '2px solid #fff',
            boxShadow: '0 0 0 2px ' + (user.profile_color || '#ccc') + '44'
          }"
        ></div>
        <div>
          <h5 class="mb-0 fw-bold">{{ user.username }}</h5>
          <small class="text-muted">나의 프로필</small>
        </div>
      </div>

      <div class="mb-4">
        <h6 class="fw-semibold mb-2">관심 카테고리</h6>
        <div class="d-flex flex-wrap gap-2">
          <span v-for="cat in user.favorite_categories" :key="cat.id"
            class="badge rounded-pill"
            :style="{
              background: cat.color || '#eee',
              color: '#fff',
              fontWeight: 'bold',
              fontSize: '0.92rem'
            }"
          >
            {{ cat.name }}
          </span>
        </div>
      </div>

      <hr />

      <div class="mb-3">
        <h6 class="fw-semibold">좋아요한 책</h6>
        <ul class="list-group list-group-flush small">
          <li
            v-for="book in user.liked_books"
            :key="book.id"
            class="list-group-item px-0 py-1 border-0"
          >
            <i class="bi bi-heart-fill text-danger me-1"></i>
            {{ book.title }}
          </li>
          <li v-if="!user.liked_books?.length" class="text-muted small list-group-item px-0 py-1 border-0">없음</li>
        </ul>
      </div>

      <div class="mb-3">
        <h6 class="fw-semibold">읽은 책</h6>
        <ul class="list-group list-group-flush small">
          <li
            v-for="book in user.read_books"
            :key="book.id"
            class="list-group-item px-0 py-1 border-0"
          >
            <i class="bi bi-check2-circle text-primary me-1"></i>
            {{ book.title }}
          </li>
          <li v-if="!user.read_books?.length" class="text-muted small list-group-item px-0 py-1 border-0">없음</li>
        </ul>
      </div>

      <!-- 좋아요한 스레드 추가 가능 -->
      <!--
      <div class="mb-3">
        <h6 class="fw-semibold">좋아요한 스레드</h6>
        <ul class="list-group list-group-flush small">
          <li
            v-for="thread in user.liked_threads"
            :key="thread.id"
            class="list-group-item px-0 py-1 border-0"
          >
            <i class="bi bi-star-fill text-warning me-1"></i>
            {{ thread.title }}
          </li>
          <li v-if="!user.liked_threads?.length" class="text-muted small list-group-item px-0 py-1 border-0">없음</li>
        </ul>
      </div>
      -->
    </div>
  </div>
</template>
