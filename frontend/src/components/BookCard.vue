<template>
  <div class="card shadow-sm h-100 border border-2 border-dark">
    <!-- 1. 책 커버 이미지 (cover 필드만 사용) -->
    <img
      v-if="book.cover"
      :src="book.cover"
      alt="Book Cover"
      class="card-img-top"
      style="object-fit: cover; height: 200px;"
    />
    <div class="card-body pb-0">
      <h5 class="card-title fw-bold">{{ book.title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ book.author }}</h6>
      <p class="card-text small text-truncate">{{ book.summary }}</p>
    </div>
    <hr class="m-0 border-2 border-dark" />
    <div class="card-footer bg-white border-top-0 pt-2 pb-2">
      <span class="small">댓글 {{ book.comments_count ?? 0 }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  book: Object
})
console.log(book.cover)
</script>
