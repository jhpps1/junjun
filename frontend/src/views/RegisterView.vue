<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-teal-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-white p-10 rounded-xl shadow-2xl">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          회원가입
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">아이디</label>
            <input id="username" name="username" type="text" v-model="username" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="아이디 (3자 이상)">
          </div>
          <div>
            <label for="email" class="sr-only">이메일</label>
            <input id="email" name="email" type="email" v-model="email" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="이메일">
          </div>
          <div>
            <label for="password" class="sr-only">비밀번호</label>
            <input id="password" name="password" type="password" v-model="password" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="비밀번호 (6자 이상)">
          </div>
          <div>
            <label for="password-confirm" class="sr-only">비밀번호 확인</label>
            <input id="password-confirm" name="password-confirm" type="password" v-model="passwordConfirm" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 focus:z-10 sm:text-sm" placeholder="비밀번호 확인">
          </div>
        </div>

        <div class="flex items-center mt-4">
          <label for="profileColor" class="text-sm font-medium text-gray-700 mr-3">프로필 색상:</label>
          <input id="profileColor" name="profileColor" type="color" v-model="profileColor" class="h-10 w-16 rounded-md border border-gray-300 cursor-pointer focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>

        <div v-if="errorMessage" class="text-red-500 text-sm text-center">
          {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="text-green-600 text-sm text-center">
          {{ successMessage }}
        </div>

        <div>
          <button type="submit" :disabled="isLoading || !isFormValid" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 disabled:bg-emerald-300">
            <span v-if="isLoading" class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-if="isLoading">가입 처리 중...</span>
            <span v-else>회원가입</span>
          </button>
        </div>
      </form>
      <p class="mt-2 text-center text-sm text-gray-600">
        이미 계정이 있으신가요? 
        <RouterLink to="/login" class="font-medium text-emerald-600 hover:text-emerald-500">
          로그인
        </RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth'; // auth 스토어 가져오기

const router = useRouter();
const authStore = useAuthStore(); // auth 스토어 인스턴스

const username = ref('');
const email = ref('');
const password = ref('');
const passwordConfirm = ref('');
const profileColor = ref('#34D399'); // 기본 프로필 색상 (에메랄드 계열)
const errorMessage = ref('');
const successMessage = ref('');
const isLoading = ref(false);

const isFormValid = computed(() => {
  return (
    username.value.length >= 3 &&
    email.value.includes('@') && // 간단한 이메일 형식 검사
    password.value.length >= 6 &&
    password.value === passwordConfirm.value
  );
});

const handleRegister = async () => {
  errorMessage.value = '';
  successMessage.value = '';
  if (!isFormValid.value) {
    errorMessage.value = '입력 정보를 다시 확인해주세요. 아이디는 3자 이상, 비밀번호는 6자 이상이어야 하며, 비밀번호가 일치해야 합니다.';
    return;
  }

  isLoading.value = true;
  try {
    const userData = {
      username: username.value,
      email: email.value,
      password: password.value,
      profile_color: profileColor.value, // 백엔드에서 받는 필드명 확인 필요 (profile_color 또는 profileColor)
    };

    const responseData = await authStore.register(userData);
    
    // 성공 메시지 설정 (백엔드 응답에 따라 수정 가능)
    successMessage.value = responseData.message || '회원가입이 성공적으로 완료되었습니다. 로그인 페이지로 이동합니다.';
    
    // 성공 후 로그인 페이지로 리디렉션 (2초 후)
    setTimeout(() => {
      router.push('/login');
    }, 2000);

  } catch (error) {
    errorMessage.value = error.message || '회원가입 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.';
    console.error('Registration failed in component:', error);
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
