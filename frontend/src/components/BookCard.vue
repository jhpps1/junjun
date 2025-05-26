<!-- src/components/BookCard.vue -->
<template>
  <div class="card h-100">
    <div class="card-body">
      <div class="fw-bold h5">{{ book.title }}</div>
      <div class="text-muted small">저자 {{ book.author }}</div>
    </div>
    <div class="card-footer text-center small" style="height: 2.5rem; overflow: hidden;">
      <transition-group name="comment-slide" tag="div">
        <div :key="currentCommentIdx" class="comment-slide">
          "{{ book.comments[currentCommentIdx] }}"
        </div>
      </transition-group>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
const props = defineProps({ book: Object })

const currentCommentIdx = ref(0)
let interval = null

onMounted(() => {
  if (props.book.comments && props.book.comments.length > 1) {
    interval = setInterval(() => {
      currentCommentIdx.value = (currentCommentIdx.value + 1) % props.book.comments.length
    }, 2000)
  }
})
onUnmounted(() => clearInterval(interval))
watch(() => props.book, () => { currentCommentIdx.value = 0 })
</script>
<style scoped>
.comment-slide {
  transition: all 0.5s;
}
.comment-slide-leave-active,
.comment-slide-enter-active {
  transition: all 0.5s;
}
.comment-slide-enter-from {
  opacity: 0;
  transform: translateY(1rem);
}
.comment-slide-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.comment-slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.comment-slide-leave-to {
  opacity: 0;
  transform: translateY(-1rem);
}
</style>
