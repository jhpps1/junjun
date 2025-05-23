<template>
  <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <!-- 글 작성 섹션 토글 버튼 -->
    <div class="mb-8 text-center">
      <button 
        @click="showWriteForm = !showWriteForm"
        class="px-6 py-3 bg-emerald-500 text-white font-semibold rounded-lg shadow-md hover:bg-emerald-600 transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2"
      >
        {{ showWriteForm ? '작성 취소' : '새 글 작성하기' }}
      </button>
    </div>

    <!-- 글 작성 폼 -->
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="opacity-0 transform -translate-y-4"
      enter-to-class="opacity-100 transform translate-y-0"
      leave-active-class="transition ease-in duration-200"
      leave-from-class="opacity-100 transform translate-y-0"
      leave-to-class="opacity-0 transform -translate-y-4"
    >
      <ThreadWriteSection v-if="showWriteForm" @thread-submitted="handleThreadSubmitted" class="mb-12" />
    </transition>

    <!-- 글 목록 -->
    <ThreadList :key="threadListKey" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ThreadList from './ThreadList.vue'
import ThreadWriteSection from './ThreadWriteSection.vue'

const showWriteForm = ref(false)
const threadListKey = ref(0) // 글 목록을 강제로 다시 렌더링하기 위한 키

const handleThreadSubmitted = () => {
  showWriteForm.value = false // 폼 숨기기
  threadListKey.value++ // 글 목록 새로고침 (키 변경)
}
</script>
