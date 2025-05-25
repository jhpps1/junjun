<template>
  <div class="flex flex-wrap gap-4 justify-center py-16">
    <div
      v-for="cat in categories"
      :key="cat.id"
      class="p-6 min-w-[120px] min-h-[80px] rounded-full w-28 h-28 shadow-md font-bold text-lg flex flex-col items-center justify-center hover:scale-105 transition hover:shadow-xl hover:scale-110 transition"
      :style="{ backgroundColor: cat.color, color: getTextColor(cat.color) }"
    >
      <span class="mb-1">{{ cat.name }}</span>
      <!-- 색상 hex값을 소문자로 한 번 보여줄 수도 있음 -->
      <span class="text-xs opacity-70">{{ cat.color }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const categories = ref([])

onMounted(async () => {
  const res = await axios.get('/api/categories/')
  categories.value = res.data
})

// 컬러에 따라 텍스트 색상 자동 반전
function getTextColor(bg) {
  if (!bg) return '#111'
  // 단순 명도에 따라 검/흰 자동
  bg = bg.replace('#', '')
  const r = parseInt(bg.substr(0,2),16)
  const g = parseInt(bg.substr(2,2),16)
  const b = parseInt(bg.substr(4,2),16)
  const yiq = (r*299 + g*587 + b*114) / 1000
  return yiq >= 140 ? '#222' : '#fff'
}
</script>
