<template>
  <div 
    v-if="user"
    class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-sm font-medium shadow-sm"
    :style="{ backgroundColor: user.profile_color || '#E0E0E0' }"
  >
    <!-- 아바타 이미지 (선택 사항) -->
    <!-- <img v-if="user.avatar_url" :src="user.avatar_url" alt="" class="w-5 h-5 rounded-full"> -->
    <span 
      class="leading-none"
      :style="{ color: getContrastingTextColor(user.profile_color || '#E0E0E0') }"
    >
      {{ user.username || '사용자' }}
    </span>
  </div>
</template>

<script setup>
const props = defineProps({
  user: Object
})

// 배경색에 따라 적절한 텍스트 색상(검정 또는 흰색)을 반환하는 함수
function getContrastingTextColor(hexColor) {
  if (!hexColor) return '#000000';
  const r = parseInt(hexColor.slice(1, 3), 16);
  const g = parseInt(hexColor.slice(3, 5), 16);
  const b = parseInt(hexColor.slice(5, 7), 16);
  // HSP (Highly Sensitive Poo) equation from http://alienryderflex.com/hsp.html
  const hsp = Math.sqrt(
    0.299 * (r * r) +
    0.587 * (g * g) +
    0.114 * (b * b)
  );
  // HSP 값이 127.5보다 크면 밝은 색이므로 어두운 텍스트, 작으면 어두운 색이므로 밝은 텍스트
  return hsp > 127.5 ? '#000000' : '#FFFFFF';
}
</script>

<style scoped>
/* 필요한 경우 추가 스타일 */
</style>
