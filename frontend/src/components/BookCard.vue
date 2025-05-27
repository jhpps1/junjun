<template>
  <div class="book-card">
    <img v-if="book.cover" :src="book.cover" class="book-cover" alt="책커버" />
    <div v-else class="cover-placeholder">[책 아이콘]</div>
    <div class="author">작가<br>{{ book.author }}</div>
    <div class="title-row">
      <span class="title">{{ book.title }}</span>
      <span class="cat-badge" :style="{ background: book.category.color }">
        {{ book.category.name }}
      </span>
    </div>
    <div class="divider"></div>
    <div class="comment-row">댓글 {{ book.comments.length }}개 캐러셀</div>
  </div>
</template>

<script setup>
defineProps({ book: Object })
</script>

<style scoped>
.book-card {
  width: 210px; min-height: 265px;
  border: 1.5px solid #111; border-radius: 8px;
  display: flex; flex-direction: column; align-items: center;
  justify-content: flex-start;
  background: #fff;
  font-family: 'SUIT', sans-serif;
}
.book-cover, .cover-placeholder {
  width: 48px; height: 48px; margin: 1.5rem auto 1rem auto;
  display: block;
}
.cover-placeholder { background: #eee; border-radius: 8px; color: #999; display: flex; align-items: center; justify-content: center; }
.author { font-size: 1rem; color: #222; margin-bottom: 0.3rem; }
.title-row {
  display: flex; align-items: center; justify-content: center;
  gap: 0.5rem;
  margin-bottom: 0.2rem;
}
.title {
  font-size: 1.2rem; font-weight: bold; color: #111;
}
.cat-badge {
  padding: 0.16em 0.75em;
  border-radius: 10px;
  color: #111;
  font-size: 0.92rem;
  font-weight: 500;
  border: 1.5px solid #222;
  background: #f7f7f7;
}
.divider {
  width: 95%; border-bottom: 1.5px solid #111; margin: 10px 0;
}
.comment-row {
  font-size: 0.95rem; color: #555; margin-bottom: 1rem;
}
</style>
