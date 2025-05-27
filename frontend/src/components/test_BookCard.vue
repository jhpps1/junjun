<template>
  <div class="book-card bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">    <img 
      :src="book.cover" 
      :alt="book.title"
      class="w-full h-48 object-cover"
      loading="lazy"
    />
    <div class="p-3">
      <h3 class="font-bold text-base mb-1 line-clamp-2">{{ book.title }}</h3>
      <p class="text-gray-600 text-sm mb-1 line-clamp-1">{{ book.author }}</p>
      <p class="text-sm text-gray-500 line-clamp-1">{{ book.publisher }}</p>
      <div class="mt-1 text-xs">
        <span class="text-blue-600">{{ formatDate(book.pubDate) }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  book: {
    type: Object,
    required: true
  }
})

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date)
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
