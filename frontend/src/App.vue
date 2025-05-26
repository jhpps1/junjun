<template>
  <NavBar />
  <main>
    <PopularSection />
    <RecommendSection />
    <CategorySection />
    <CommunitySection />
  </main>
</template>
<script setup>
import NavBar from './components/NavBar.vue'
import PopularSection from './views/PopularSection.vue'
import RecommendSection from './views/RecommendSection.vue'
import CategorySection from './views/CategorySection.vue'
import CommunitySection from './views/CommunitySection.vue'
</script>
