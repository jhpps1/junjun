<template>
  <section class="py-5" id="section-2">
    <div class="container">
      <h2 class="mb-4 text-center fw-bold text-secondary">
        카테고리별 컬러 팔레트
      </h2>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-4">
        <div
          class="col"
          v-for="category in categories"
          :key="category.pk"
        >
          <div class="card text-center shadow-sm h-100 border-0">
            <div
              class="rounded-circle mx-auto mt-4 mb-2"
              :style="{
                backgroundColor: category.color,
                width: '56px',
                height: '56px',
                border: '3px solid #fff',
                boxShadow: '0 0 0 2px ' + category.color + '44'
              }"
            ></div>
            <div class="card-body">
              <h5 class="card-title mb-1 fw-semibold" :style="{ color: category.color }">
                {{ category.name }}
              </h5>
            </div>
          </div>
        </div>
      </div>
      <div v-if="!categories.length" class="text-center py-5 text-muted">
        카테고리 정보를 불러오는 중...
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'

const categories = ref([])

onMounted(async () => {
  const res = await axios.get('/api/categories/')
  categories.value = res.data.results ?? res.data
})
</script>
