<template>
  <section id="community" class="container py-5">
    <div class="text-center mb-4">
      <div class="fw-bold">Tagline</div>
      <h2 class="fw-bold">커뮤니티</h2>
      <div class="text-muted mb-2">커뮤니티 설명</div>
    </div>
    <!-- 세로 캐러셀 (샘플: 단순 위아래 이동 버튼) -->
    <div class="d-flex flex-column align-items-center">
      <button class="btn btn-outline-secondary mb-2" @click="prev">
        <i class="bi bi-arrow-up"></i>
      </button>
      <div class="w-100" style="max-width:500px;">
        <div v-if="current === 0" class="card p-4 mb-3">
          <div class="fw-bold mb-1">내 정보</div>
          <div class="small text-muted mb-2">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br>
            <i class="bi bi-geo-alt"></i> Location &nbsp; <i class="bi bi-file-earmark"></i> Contract Type
          </div>
        </div>
        <div v-else-if="current === 1" class="card p-4 mb-3">
          <div class="fw-bold mb-1">스레드 세로 carousel 순회</div>
          <div class="small text-muted">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </div>
        </div>
        <div v-else-if="current === 2" class="card p-4 mb-3">
          <div class="fw-bold mb-1">Pal 찾기</div>
          <div class="small text-muted">
            나와 비슷한 색의 펄 / 가장 다른 펄의 책을 보여줌
          </div>
        </div>
      </div>
      <button class="btn btn-outline-secondary mt-2" @click="next">
        <i class="bi bi-arrow-down"></i>
      </button>
    </div>
  </section>
</template>
<script setup>
import { ref } from 'vue'
const current = ref(0)
function prev() { if (current.value > 0) current.value-- }
function next() { if (current.value < 2) current.value++ }
</script>
