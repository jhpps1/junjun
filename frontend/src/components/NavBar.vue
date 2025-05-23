<template>
  <nav class="fixed top-0 left-0 w-full z-50 bg-white border-b">
    <div class="flex gap-8 px-8 py-4">
      <button
        v-for="item in menu"
        :key="item.id"
        @click="scrollToSection(item.id)"
        class="font-bold hover:text-indigo-500 transition"
      >
        {{ item.label }}
      </button>
    </div>
  </nav>
</template>
<script setup>
const menu = [
  { id: "section-1", label: "소개" },
  { id: "section-2", label: "카테고리" },
  { id: "section-3", label: "추천도서" },
  { id: "section-4", label: "커뮤니티" },
  // ... 필요에 따라 확장
]

function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "start" })
  }
}
</script>
