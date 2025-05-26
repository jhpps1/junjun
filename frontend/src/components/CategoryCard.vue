<template>
  <div class="card h-100">
    <div class="card-body d-flex flex-column align-items-center justify-content-center">
      <span class="fw-bold" :style="{ color: category.color }">{{ category.name }}</span>
      <div class="mt-3 mb-1">90,000 <span class="text-success">▲ 100%</span></div>
      <div class="small text-muted">View report</div>
    </div>
  </div>
</template>
<script setup>
defineProps({ category: Object })
</script>
