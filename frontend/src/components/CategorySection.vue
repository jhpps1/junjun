<template>
  <section id="category" class="py-5">
    <div class="container">
      <h2 class="text-center mb-4">카테고리</h2>
      <!-- 로딩 및 에러 상태 표시 -->
      <div v-if="loading" class="text-center">
        <p>카테고리를 불러오는 중입니다...</p>
      </div>
      <div v-else-if="error" class="text-center text-danger">
        <p>{{ error }}</p>
      </div>
      <!-- 카테고리 목록 표시 -->
      <Carousel :items-to-show="5" :wrap-around="true" v-else-if="categories.length > 0">
        <Slide v-for="category in categories" :key="category.id || category.pk">
          <div class="card category-card m-2" @click="selectCategory(category.id || category.pk)">
            <img :src="category.image || defaultImage" class="card-img-top category-image" :alt="category.name">
            <div class="card-body text-center">
              <h5 class="card-title">{{ category.name }}</h5>
            </div>
          </div>
        </Slide>
        <template #addons>
          <Navigation />
        </template>
      </Carousel>
      <div v-else class="text-center">
        <p>표시할 카테고리가 없습니다.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Carousel, Navigation, Slide } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';
import { API_URL } from '../consts';

const defaultImage = 'https://via.placeholder.com/150x150/CCCCCC/FFFFFF?text=No+Image';
const categories = ref([]);
const loading = ref(true);
const error = ref(null);

// 카테고리 데이터 불러오기
onMounted(async () => {
  try {
    loading.value = true;
    error.value = null;
    
    // 백엔드 API에서 카테고리 데이터 불러오기
    // config/urls.py에 따라 api/ 접두사가 붙고, books/urls.py에 따라 categories/ 경로 사용
    const res = await axios.get(`${API_URL}/categories/`);
    
    if (Array.isArray(res.data)) {
      categories.value = res.data.map(cat => ({
        ...cat,
        id: cat.pk || cat.id, // pk 또는 id 필드 통일
        image: cat.image || defaultImage // 이미지가 없으면 기본 이미지 사용
      }));
    } else {
      console.error("카테고리 정보가 배열 형식이 아닙니다:", res.data);
      error.value = "카테고리 정보 형식이 올바르지 않습니다.";
    }
  } catch (err) {
    console.error("카테고리 정보를 가져오는 데 실패했습니다:", err);
    error.value = "카테고리 정보를 가져오는 데 실패했습니다.";
  } finally {
    loading.value = false;
  }
});

const selectCategory = (categoryId) => {
  console.log(`Category ${categoryId} selected`);
  // TODO: 카테고리 선택 시 동작 구현 (예: 해당 카테고리 페이지로 이동 또는 필터링)
};
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2; /* Standard property */
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.group-hover\:line-clamp-none:hover {
  -webkit-line-clamp: unset;
  line-clamp: unset; /* Standard property */
}
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.group-hover\:whitespace-normal:hover {
  white-space: normal;
}

.category-card {
  cursor: pointer;
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
  border: 1px solid #eee;
  /* min-height: 100px; 제거 또는 조정 */
  display: flex;
  flex-direction: column;
  /* justify-content: center; 제거 또는 조정 */
  align-items: center;
  overflow: hidden; /* 이미지가 카드를 벗어나지 않도록 */
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.category-image {
  width: 100%; /* 카드 너비에 맞춤 */
  height: 120px; /* 이미지 높이 고정, 필요에 따라 조정 */
  object-fit: cover; /* 이미지 비율 유지하며 채우기 */
}

.card-body {
  padding: 0.75rem;
  width: 100%; /* 카드 본문 너비 확보 */
}

.card-title {
  font-size: 0.9rem; /* 글꼴 크기 약간 줄임 */
  font-weight: bold;
  margin-bottom: 0; /* 제목 아래 여백 제거 */
  white-space: nowrap; /* 제목이 길 경우 한 줄로 표시 */
  overflow: hidden;
  text-overflow: ellipsis; /* 넘치는 텍스트는 ...으로 표시 */
}

/* vue3-carousel 커스텀 (필요한 경우) */
:deep(.carousel__prev),
:deep(.carousel__next) {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  color: white;
  width: 30px; /* 버튼 크기 조정 */
  height: 30px; /* 버튼 크기 조정 */
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep(.carousel__prev:hover),
:deep(.carousel__next:hover) {
  background-color: rgba(0, 0, 0, 0.7);
}

:deep(.carousel__icon) {
    width: 16px; /* 아이콘 크기 조정 */
    height: 16px; /* 아이콘 크기 조정 */
}

/* 슬라이드 간 간격을 위한 스타일 */
.carousel__slide {
  padding: 0 5px; /* 슬라이드 좌우 패딩 */
}

</style>
