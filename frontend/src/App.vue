<script setup>
import NavBar from './components/NavBar.vue'
import CategorySection from './components/CategorySection.vue'
import BookRecommendSection from './components/BookRecommendSection.vue'
import CommunitySection from './components/CommunitySection.vue'
</script>

<template>
  <NavBar />
  <main class="pt-20">
    <section id="section-1" class="min-h-[80vh] flex flex-col items-center justify-center bg-gray-100">
      <h1 class="text-3xl font-bold mb-8">1. 서비스 소개</h1>
      <!-- 소개 내용 등 -->
    </section>
    <section id="section-2" class="min-h-[80vh] bg-[#E3F6F5]">
      <h1 class="text-3xl font-bold text-center py-10">2. 카테고리 색상 시각화</h1>
      <CategorySection />
    </section>
    <section id="section-3" class="min-h-[80vh] bg-[#F9F5FF]">
      <h1 class="text-3xl font-bold text-center py-10">3. 추천도서 영역</h1>
      <BookRecommendSection />
    </section>
    <section id="section-4" class="min-h-[80vh] bg-[#FFF7F0]">
      <h1 class="text-3xl font-bold text-center py-10">4. 커뮤니티</h1>
      <CommunitySection />
    </section>
    <!-- ...필요시 추가 -->
  </main>
</template>
