<template>
  <div class="container-fluid px-0">
    <PopularSection />
    <RecommendSection />
    <CategorySection />
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
