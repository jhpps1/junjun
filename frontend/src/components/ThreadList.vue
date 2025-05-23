<template>
  <div>
    <div v-if="loading" class="text-center py-10">
      <p class="text-lg text-gray-500">게시글을 불러오는 중...</p>
      <!-- 스켈레톤 UI 추가 (선택 사항) -->
    </div>
    <div v-else-if="error" class="text-center py-10">
      <p class="text-lg text-red-500">게시글을 불러오는 데 실패했습니다.</p>
    </div>
    <div v-else-if="threads.length === 0" class="text-center py-10">
      <p class="text-lg text-gray-500">아직 게시글이 없습니다. 첫 글을 작성해보세요!</p>
    </div>
    <div v-else class="space-y-6">
      <div 
        v-for="thread in threads" 
        :key="thread.id" 
        class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300"
      >
        <div class="p-6">
          <div class="flex items-center mb-4">
            <UserBadge :user="thread.user" />
            <span class="ml-auto text-xs text-gray-400">{{ formatDate(thread.created_at) }}</span>
          </div>
          <h2 class="text-xl font-semibold text-gray-800 mb-2 hover:text-emerald-600 transition-colors cursor-pointer">{{ thread.title }}</h2>
          <p class="text-gray-600 leading-relaxed line-clamp-3 mb-4">{{ thread.content }}</p>
          <div class="flex items-center text-sm text-gray-500">
            <!-- 좋아요, 댓글 수 등 추가 정보 표시 가능 -->
            <span>댓글 {{ thread.comment_count || 0 }}개</span>
            <button class="ml-auto text-emerald-500 hover:text-emerald-600 font-medium">더 보기</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 페이지네이션 UI 추가 (선택 사항) -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import UserBadge from './UserBadge.vue'

const threads = ref([])
const loading = ref(true)
const error = ref(null)

const fetchThreads = async () => {
  loading.value = true
  error.value = null
  try {
    // const response = await axios.get(`${API_URL}/community/threads/`); // API_URL 정의 필요 또는 스토어 사용
    // 임시 데이터 사용 (실제 API 호출 시 아래 로직은 응답 데이터 구조에 맞게 수정)
    const res = {
      data: {
        results: [
          { id: 1, title: '첫 번째 글입니다!', content: '내용이 들어갑니다...', author_nickname: '익명1', created_at: '2024-05-22T10:00:00Z', comment_count: 2, views: 15 },
          { id: 2, title: 'Vue3 질문 있습니다.', content: 'Composition API 사용법 관련해서...', author_nickname: '개발자꿈나무', created_at: '2024-05-23T11:30:00Z', comment_count: 5, views: 30 },
        ]
      }
    };
    const responseData = res.data.results ?? res.data; // 옵셔널 체이닝 및 nullish coalescing 사용
    if (Array.isArray(responseData)) {
      threads.value = responseData.map(thread => ({
        ...thread,
        created_at: new Date(thread.created_at).toLocaleDateString(),
      }));
    } else {
      console.error('Error fetching threads: Response data is not an array', res.data);
      threads.value = []; // 배열이 아니면 빈 배열로 초기화
      error.value = '게시글 데이터를 불러오는 데 실패했습니다 (데이터 형식 오류).';
    }
  } catch (err) {
    console.error('Error fetching threads:', err);
    error.value = '게시글을 불러오는 중 오류가 발생했습니다.';
    threads.value = []; // 오류 발생 시 빈 배열로 초기화
  } finally {
    loading.value = false;
  }
}

onMounted(fetchThreads)

const formatDate = (dateString) => {
  if (!dateString) return ''
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
}

// 부모 컴포넌트에서 호출할 수 있도록 함수 노출 (선택 사항)
// defineExpose({ fetchThreads })
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
