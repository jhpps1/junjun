<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-teal-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-white p-10 rounded-xl shadow-2xl">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          로그인
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">아이디</label>
            <input id="username" name="username" type="text" v-model="username" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="아이디">
          </div>
          <div>
            <label for="password" class="sr-only">비밀번호</label>
            <input id="password" name="password" type="password" v-model="password" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="비밀번호">
          </div>
        </div>

        <div v-if="errorMessage" class="text-red-500 text-sm text-center">
          {{ errorMessage }}
        </div>

        <div>
          <button type="submit" :disabled="isLoading" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 disabled:bg-emerald-300">
            <span v-if="isLoading" class="absolute left-0 inset-y-0 flex items-center pl-3">
              <!-- 로딩 스피너 아이콘 (예: Heroicons의 ArrowPathIcon) -->
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-if="isLoading">로그인 중...</span>
            <span v-else>로그인</span>
          </button>
        </div>
      </form>
      <p class="mt-2 text-center text-sm text-gray-600">
        계정이 없으신가요? 
        <RouterLink to="/register" class="font-medium text-emerald-600 hover:text-emerald-500">
          회원가입
        </RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth'; // 경로 수정되었을 수 있으니 확인

const username = ref('');
const password = ref('');
const authStore = useAuthStore();
const router = useRouter();
const errorMessage = ref('');
const isLoading = ref(false);

const handleLogin = async () => {
  errorMessage.value = '';
  isLoading.value = true;
  try {
    // authStore의 login 액션 사용
    await authStore.login(username.value, password.value);
    // 로그인 성공 후 홈으로 리디렉션
    // 사용자가 특정 페이지로 리디렉션되기를 원했다면 그 정보를 사용할 수 있습니다.
    // const redirectPath = router.currentRoute.value.query.redirect || '/';
    router.push('/'); 
  } catch (error) {
    // 스토어에서 발생한 에러 메시지 사용 또는 기본 메시지
    errorMessage.value = error.message || '로그인에 실패했습니다. 아이디 또는 비밀번호를 확인해주세요.';
    console.error('Login failed:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
/* 필요한 경우 여기에 스타일 추가 */
.min-h-screen {
  min-height: calc(100vh - 4rem); /* NavBar 높이(h-16 = 4rem) 제외 */
}
</style>