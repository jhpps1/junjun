<template>
  <div class="card shadow-sm h-100 border border-2 border-dark">
    <div class="card-body pb-0">
      <h5 class="card-title fw-bold">{{ book.title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ book.author }}</h6>
      <p class="card-text small text-truncate">{{ book.description }}</p>
    </div>
    <hr class="m-0 border-2 border-dark" />
    <div class="card-footer bg-white border-top-0 pt-2 pb-2">
      <div class="d-flex justify-content-between align-items-center">
        <span class="small">댓글 {{ book.comments_count ?? 0 }}</span>
        <span class="small text-secondary">평점 {{ book.rating ?? '-' }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  book: Object
})
</script>
