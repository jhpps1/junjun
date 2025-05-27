<template>
  <div class="container-fluid px-0">
    <!-- 인기 도서 섹션 -->
    <PopularSection />

    <!-- 추천 도서 섹션 -->
    <RecommendSection />

    <!-- 카테고리 섹션 -->
    <CategorySection />

    <!-- 커뮤니티 섹션 -->
    <CommunitySection />
  </div>
</template>

<script setup>
import PopularSection from '../components/PopularSection.vue'
import RecommendSection from '../components/RecommendSection.vue'
import CategorySection from '../components/CategorySection.vue'
import CommunitySection from '../components/CommunitySection.vue'

</script>

<style scoped>
/* 페이지 전체 여백 및 구분 */
.container-fluid {
  background: #fff;
  min-height: 100vh;
  padding-bottom: 40px;
}
</style>
