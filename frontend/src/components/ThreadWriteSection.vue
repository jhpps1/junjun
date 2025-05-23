<template>
  <form @submit.prevent="submitThread" class="bg-white p-6 sm:p-8 rounded-xl shadow-lg space-y-6 max-w-2xl mx-auto">
    <div>
      <label for="thread-title" class="block text-sm font-medium text-gray-700 mb-1">제목</label>
      <input 
        id="thread-title"
        v-model="title" 
        placeholder="글 제목을 입력해주세요" 
        class="w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-emerald-500 focus:border-emerald-500 transition duration-150 ease-in-out"
        required 
      />
    </div>
    <div>
      <label for="thread-content" class="block text-sm font-medium text-gray-700 mb-1">내용</label>
      <textarea 
        id="thread-content"
        v-model="content" 
        placeholder="자유롭게 이야기를 나눠보세요!"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-emerald-500 focus:border-emerald-500 transition duration-150 ease-in-out min-h-[150px] resize-none"
        required 
      />
    </div>
    <div class="flex items-center justify-end">
      <button 
        type="submit" 
        :disabled="isSubmitting"
        class="px-6 py-2 bg-emerald-500 text-white font-semibold rounded-lg shadow-md hover:bg-emerald-600 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {{ isSubmitting ? '등록 중...' : '글 등록' }}
      </button>
    </div>
    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="successMessage" class="mt-3 text-sm text-green-600 bg-green-50 p-3 rounded-md">{{ successMessage }}</div>
    </transition>
    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="errorMessage" class="mt-3 text-sm text-red-600 bg-red-50 p-3 rounded-md">{{ errorMessage }}</div>
    </transition>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const title = ref('')
const content = ref('')
const successMessage = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)

const emit = defineEmits(['thread-submitted'])

async function submitThread() {
  if (isSubmitting.value) return

  isSubmitting.value = true
  successMessage.value = ''
  errorMessage.value = ''

  try {
    // 실제 API 엔드포인트와 요청 데이터 구조에 맞게 수정 필요
    await axios.post('/api/threads/', { 
      title: title.value, 
      content: content.value,
      // user_id: 1 // 예시: 현재 로그인한 사용자 ID (실제 구현 필요)
    })
    successMessage.value = '게시글이 성공적으로 등록되었습니다! 잠시 후 목록이 새로고침됩니다.'
    title.value = ''
    content.value = ''
    
    // 부모 컴포넌트에 이벤트 전달
    setTimeout(() => {
      emit('thread-submitted')
      successMessage.value = '' // 메시지 초기화
    }, 2000) // 2초 후 실행

  } catch (err) {
    console.error("글 작성 실패:", err.response || err);
    errorMessage.value = err.response?.data?.detail || err.response?.data?.message || '글 등록 중 오류가 발생했습니다. 다시 시도해주세요.'
    // 특정 필드 에러 처리 (예시)
    // if (err.response?.data?.title) errorMessage.value += ` 제목: ${err.response.data.title.join(', ')}`;
    // if (err.response?.data?.content) errorMessage.value += ` 내용: ${err.response.data.content.join(', ')}`;
  } finally {
    isSubmitting.value = false
  }
}
</script>
