<template>
  <div class="grid grid-cols-2 gap-4">
    <div
      v-for="cat in categories"
      :key="cat.id"
      class="p-4 rounded-2xl shadow-md text-white font-bold text-lg flex items-center"
      :style="{ backgroundColor: cat.color }"
    >
      <span>{{ cat.name }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'

const categories = ref([])

onMounted(async () => {
  const res = await axios.get('/api/categories/')
  categories.value = res.data
})
</script>
