<template>
  <nav class="fixed top-0 left-0 w-full z-50 bg-white/80 backdrop-blur-md shadow-sm border-b border-gray-200/80">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <RouterLink to="/" @click.prevent="scrollToSection('section-1', true)" class="text-2xl font-bold text-emerald-600 hover:text-emerald-700 transition-colors">
            Book Palette
          </RouterLink>
        </div>

        <div class="flex items-center space-x-1">
          <button
            v-for="item in menu"
            :key="item.id"
            @click="scrollToSection(item.id)"
            class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:bg-emerald-50 hover:text-emerald-600 transition-all duration-200"
            :class="{ 'bg-emerald-100 text-emerald-700': activeSection === item.id }"
          >
            {{ item.label }}
          </button>
        </div>

        <div class="flex items-center space-x-3">
          <!-- 로그인하지 않았을 때 -->
          <template v-if="!authStore.isLoggedIn">
            <RouterLink 
              to="/login" 
              class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 rounded-md transition-colors duration-200"
            >
              로그인
            </RouterLink>
            <RouterLink 
              to="/register" 
              class="px-4 py-2 bg-emerald-500 text-white text-sm font-medium rounded-md hover:bg-emerald-600 transition-colors duration-200 shadow-sm"
            >
              회원가입
            </RouterLink>
          </template>
          <!-- 로그인했을 때 -->
          <template v-else>
            <UserBadge :user="authStore.currentUser" class="mr-2" />
            <RouterLink
              to="/mypage" 
              class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 rounded-md transition-colors duration-200"
            >
              마이페이지
            </RouterLink>
            <button
              @click="handleLogout"
              class="px-4 py-2 bg-red-500 text-white text-sm font-medium rounded-md hover:bg-red-600 transition-colors duration-200 shadow-sm"
            >
              로그아웃
            </button>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'; // computed 추가 (이미 있다면 유지)
import { RouterLink, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth'; // auth 스토어 가져오기
import UserBadge from './UserBadge.vue'; // UserBadge 컴포넌트 가져오기

const authStore = useAuthStore();
const router = useRouter();

const menu = [
  { id: "section-1", label: "소개" },
  { id: "section-2", label: "카테고리" },
  { id: "section-3", label: "추천도서" },
  { id: "section-4", label: "커뮤니티" }
];

const activeSection = ref('section-1');

const scrollToSection = (sectionId, isLogoClick = false) => {
  const element = document.getElementById(sectionId);
  if (element) {
    const offset = (isLogoClick || sectionId === 'section-1') ? 0 : 64; // NavBar 높이
    const bodyRect = document.body.getBoundingClientRect().top;
    const elementRect = element.getBoundingClientRect().top;
    const elementPosition = elementRect - bodyRect;
    const offsetPosition = elementPosition - offset;

    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    });
  }
};

const handleLogout = () => {
  authStore.logout(); // 스토어의 logout 액션 호출
  // router.push('/'); // logout 액션 내부에서 리디렉션 처리하므로 중복 호출 필요 없음
};

// IntersectionObserver 로직은 동일하게 유지
// ...existing code...
onMounted(() => {
  // 로그인 상태는 authStore에서 관리하므로 localStorage 직접 접근 제거
  // isLoggedIn.value = localStorage.getItem('isLoggedIn') === 'true'; // 이 줄 제거

  menu.forEach(item => {
    const section = document.getElementById(item.id);
    if (section) {
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            activeSection.value = item.id;
          }
        });
      }, observerOptions);
      observer.observe(section);
      observers.push(observer);
    }
  });
});

// ...existing code...
const observerOptions = {
  root: null,
  rootMargin: '-64px 0px -50% 0px',
  threshold: 0
};

let observers = [];

onUnmounted(() => {
  observers.forEach(observer => observer.disconnect());
});

</script>
