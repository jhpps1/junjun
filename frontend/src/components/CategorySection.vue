<template>
  <div class="flex flex-wrap gap-4 justify-center py-16">
    <div
      v-for="cat in categories"
      :key="cat.id"
      class="p-6 rounded-2xl shadow-md font-bold text-lg min-w-[150px] text-center"
      :style="{ backgroundColor: cat.color, color: '#fff' }"
    >
      {{ cat.name }}
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
</script>
