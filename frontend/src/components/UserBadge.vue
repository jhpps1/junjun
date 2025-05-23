<template>
  <div
    class="flex items-center gap-2"
    :style="{ backgroundColor: user.profile_color || '#eee', borderRadius: '2rem', padding: '0.3rem 0.8rem' }"
  >
    <span class="font-bold text-white">{{ user.username }}</span>
  </div>
</template>
<script setup>
defineProps(['user'])
</script>
