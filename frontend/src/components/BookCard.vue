<template>
  <div class="card h-100">
    <div class="card-body">
      <div class="text-center mb-2">
        <i class="bi bi-book" style="font-size: 2rem;"></i>
      </div>
      <div class="text-muted small">작가 {{ book.author }}</div>
      <div class="fw-bold h5 mt-2">{{ book.title }}</div>
      <div class="d-flex align-items-center justify-content-between mt-2">
        <span class="text-success fw-bold">100%</span>
        <span class="text-muted small">댓글 {{ comments.length }}개</span>
      </div>
    </div>
    <div class="card-footer text-center small">
      <button
        class="btn btn-outline-secondary btn-sm me-2"
        @click="prevComment"
        :disabled="currentComment === 0"
      >↑</button>
      <transition name="fade" mode="out-in">
        <span v-if="comments.length" :key="currentComment">
          {{ comments[currentComment] }}
        </span>
        <span v-else>댓글 없음</span>
      </transition>
      <button
        class="btn btn-outline-secondary btn-sm ms-2"
        @click="nextComment"
        :disabled="currentComment === comments.length - 1"
      >↓</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
const props = defineProps({
  book: { type: Object, required: true }
})
const comments = computed(() => props.book.comments || [])
const currentComment = ref(0)
function prevComment() {
  if (currentComment.value > 0) currentComment.value--
}
function nextComment() {
  if (currentComment.value < comments.value.length - 1) currentComment.value++
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
