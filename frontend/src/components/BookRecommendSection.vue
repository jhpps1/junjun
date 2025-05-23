<template>
  <div class="container mx-auto px-4 sm:px-6 lg:px-8">
    <div v-if="loading" class="text-center py-10">
      <p class="text-lg text-gray-500">추천 도서를 불러오는 중...</p>
    </div>
    <div v-else-if="error" class="text-center py-10">
      <p class="text-lg text-red-500">{{ error }}</p>
    </div>
    <div v-else-if="recommendedBooks.length === 0" class="text-center py-10">
      <p class="text-lg text-gray-500">표시할 추천 도서가 없습니다.</p>
    </div>
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-x-6 gap-y-10">
      <div
        v-for="book in recommendedBooks"
        :key="book.id || book.pk"
        class="group bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 flex flex-col overflow-hidden"
      >
        <div class="relative pt-[140%]" :style="{ backgroundColor: book.color || '#e0e0e0' }">
          <img 
            :src="book.cover_image || `https://placehold.co/300x420/e0e0e0/333333?text=${encodeURIComponent(book.title || 'Book')}`" 
            :alt="book.title"
            class="absolute top-0 left-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          />
          <div class="absolute top-2 right-2 flex flex-col space-y-2">
            <button
              @click.stop="toggleLike(book)"
              :title="book.isLiked ? '찜 해제' : '찜하기'"
              class="p-2 rounded-full bg-white/80 backdrop-blur-sm shadow-md hover:bg-emerald-100 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" :fill="book.isLiked ? book.color || 'currentColor' : 'gray'">
                <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
              </svg>
            </button>
            <button
              @click.stop="toggleRead(book)"
              :title="book.isRead ? '읽음 취소' : '읽음 표시'"
              class="p-2 rounded-full bg-white/80 backdrop-blur-sm shadow-md hover:bg-emerald-100 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" :fill="book.isRead ? book.color || 'currentColor' : 'gray'">
                <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                <path fill-rule="evenodd" d="M4 5a2 2 0 012-2h8a2 2 0 012 2v10a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h6a1 1 0 100-2H7z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
        </div>
        <div class="p-4 flex flex-col flex-grow">
          <h3 class="text-md font-semibold text-gray-800 mb-1 truncate group-hover:whitespace-normal group-hover:text-emerald-600 transition-colors">{{ book.title }}</h3>
          <p class="text-xs text-gray-500 mb-2 truncate">{{ book.author }}</p>
          <span 
            class="text-xs font-medium px-2 py-0.5 rounded-full self-start"
            :style="{ backgroundColor: book.color ? `${book.color}20` : '#e0e0e0', color: book.color || '#555' }"
          >
            {{ book.category?.name || '미분류' }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { API_URL } from '../consts';

const recommendedBooks = ref([]);
const loading = ref(true);
const error = ref(null);

async function fetchBooksAndRelations() {
  loading.value = true;
  error.value = null;
  
  try {
    // 백엔드 API에서 책 데이터 가져오기 
    // config/urls.py에 따라 api/ 접두사가 붙고, books/urls.py에 따라 books/ 경로 사용
    const booksResponse = await axios.get(`${API_URL}/books/`, {
      params: {
        is_recommended: true, // 추천 도서 필터링 (실제 백엔드 API 파라미터에 맞게 수정)
        limit: 10 // 보여줄 책 수 제한 (실제 백엔드 API 파라미터에 맞게 수정)
      }
    });

    // 관계(좋아요, 읽음) 데이터를 가져오기
    // config/urls.py에 따라 api/ 접두사가 붙고, books/urls.py에 따라 relations/ 경로 사용
    let likesResponse;
    try {
      likesResponse = await axios.get(`${API_URL}/relations/`);
    } catch (err) {
      console.warn("관계 정보를 가져오는데 실패했습니다:", err);
      // 관계 정보 실패는 치명적 실패로 간주하지 않음
      likesResponse = { data: [] };
    }

    // 데이터 형식 확인
    if (Array.isArray(booksResponse.data)) {
      const booksData = booksResponse.data;
      const likesData = Array.isArray(likesResponse.data) ? likesResponse.data : [];

      // 사용자 ID (로그인 상태에 따라 변경 필요)
      // 실제로는 auth 저장소에서 로그인 사용자 ID를 가져와야 함
      const currentUserId = null; // 로그인되지 않은 상태

      // 책 데이터와 관계 데이터 결합
      recommendedBooks.value = booksData.map(book => ({
        ...book,
        id: book.pk || book.id, // id 필드 통일
        isLiked: currentUserId ? likesData.some(like => 
          like.book === (book.pk || book.id) && 
          like.user === currentUserId && 
          like.status === 'like'
        ) : false,
        isRead: currentUserId ? likesData.some(read => 
          read.book === (book.pk || book.id) && 
          read.user === currentUserId && 
          read.status === 'read'
        ) : false,
        // 카테고리 정보가 내장되어 있지 않은 경우를 대비한 기본값 처리
        category: book.category || { name: '미분류' },
        // 표지 이미지가 없는 경우 기본 이미지 URL 사용 (실제 렌더링은 템플릿에서 처리)
        color: book.category?.color || '#e0e0e0'
      }));
    } else {
      console.error('책 데이터 형식이 올바르지 않습니다:', booksResponse.data);
      error.value = '추천 도서 정보 형식이 올바르지 않습니다.';
      recommendedBooks.value = [];
    }
  } catch (err) {
    console.error('추천 도서 정보를 가져오는 데 실패했습니다:', err);
    error.value = '추천 도서 정보를 가져오는 중 오류가 발생했습니다.';
    recommendedBooks.value = [];
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBooksAndRelations);

// 임시 구현: 실제로는 백엔드 API와 연동 필요
async function toggleLike(book) {
  // 로그인 상태 확인이 필요 (실제로는 auth 저장소에서 확인)
  const isLoggedIn = false; // 임시로 false 설정
  
  // 로그인하지 않은 경우 로그인 페이지로 이동
  if (!isLoggedIn) {
    alert('찜하기/해제는 로그인 후 이용 가능합니다.');
    // router.push('/login'); // 실제로는 라우터를 통해 로그인 페이지로 이동
    return;
  }

  // 로그인 상태라면 관계 업데이트 처리
  const originalIsLiked = book.isLiked;
  book.isLiked = !book.isLiked; // 즉시 UI 업데이트 (옵티미스틱 업데이트)

  try {
    if (book.isLiked) {
      // 찜하기 추가 요청
      await axios.post(`${API_URL}/relations/`, { 
        book: book.id || book.pk,
        status: 'like'
      });
    } else {
      // 찜하기 해제 요청 (실제로는 기존 관계 ID를 알아야 함)
      await axios.delete(`${API_URL}/relations/some-relation-id/`);
    }
  } catch (err) {
    console.error('찜하기/해제 요청 중 오류가 발생했습니다:', err);
    book.isLiked = originalIsLiked; // 실패 시 원래 상태로 되돌림
    alert('찜하기/해제 처리 중 오류가 발생했습니다.');
  }
}

// 임시 구현: 실제로는 백엔드 API와 연동 필요
async function toggleRead(book) {
  // 로그인 상태 확인이 필요 (실제로는 auth 저장소에서 확인)
  const isLoggedIn = false; // 임시로 false 설정
  
  // 로그인하지 않은 경우 로그인 페이지로 이동
  if (!isLoggedIn) {
    alert('읽음 표시는 로그인 후 이용 가능합니다.');
    // router.push('/login'); // 실제로는 라우터를 통해 로그인 페이지로 이동
    return;
  }

  // 로그인 상태라면 관계 업데이트 처리
  const originalIsRead = book.isRead;
  book.isRead = !book.isRead; // 즉시 UI 업데이트 (옵티미스틱 업데이트)

  try {
    if (book.isRead) {
      // 읽음 표시 추가 요청
      await axios.post(`${API_URL}/relations/`, { 
        book: book.id || book.pk,
        status: 'read'
      });
    } else {
      // 읽음 표시 해제 요청 (실제로는 기존 관계 ID를 알아야 함)
      await axios.delete(`${API_URL}/relations/some-relation-id/`);
    }
  } catch (err) {
    console.error('읽음 표시/해제 요청 중 오류가 발생했습니다:', err);
    book.isRead = originalIsRead; // 실패 시 원래 상태로 되돌림
    alert('읽음 표시/해제 처리 중 오류가 발생했습니다.');
  }
}
</script>

<style scoped>
.pt-\[140\%\] {
  padding-top: 140%;
}
</style>
