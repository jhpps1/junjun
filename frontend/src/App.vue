<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue' // computed 추가
import { useRoute } from 'vue-router' // useRoute 추가
import NavBar from './components/NavBar.vue'
import CategorySection from './components/CategorySection.vue'
import BookRecommendSection from './components/BookRecommendSection.vue'
import CommunitySection from './components/CommunitySection.vue'

const showScrollTop = ref(false)
const route = useRoute() // 현재 라우트 정보

// 현재 경로가 메인 페이지('/')인지 확인하는 계산된 속성
const isHomePage = computed(() => route.path === '/')

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

let observer = null

const observeFirstSection = () => {
  const section1 = document.getElementById('section-1')
  if (!section1) return

  if (observer) observer.disconnect() // 기존 observer 정리

  observer = new IntersectionObserver(
    (entries) => {
      const entry = entries[0]
      showScrollTop.value = !entry.isIntersecting && entry.boundingClientRect.bottom < 0
    },
    {
      root: null,
      threshold: 0,
    }
  )
  observer.observe(section1)
}

onMounted(() => {
  if (isHomePage.value) {
    observeFirstSection()
  }
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})

// 라우트 변경 시 section-1 관찰 로직 재실행 (isHomePage가 true일 때)
import { watch } from 'vue';
watch(isHomePage, (newValue) => {
  if (newValue) {
    // DOM 업데이트 후 실행하도록 nextTick 사용 가능성 고려
    // import { nextTick } from 'vue';
    // nextTick(() => observeFirstSection());
    // 혹은 setTimeout으로 약간의 지연을 주어 DOM이 확실히 렌더링된 후 실행
    setTimeout(() => observeFirstSection(), 0);
  } else {
    if (observer) observer.disconnect();
    showScrollTop.value = false; // 다른 페이지에서는 스크롤탑 버튼 숨김
  }
});

</script>

<template>
  <NavBar />
  <main class="pt-16">
    <!-- isHomePage가 true일 때만 기존 섹션들을 렌더링 -->
    <template v-if="isHomePage">
      <section id="section-1" class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-emerald-50 via-sky-50 to-purple-50 p-8">
        <!-- ... 기존 section-1 내용 ... -->
        <h1 class="text-5xl font-bold mb-6 text-center text-gray-800 leading-tight">
          Book Palette에 오신 것을 환영합니다!
        </h1>
        <p class="text-xl text-gray-600 text-center max-w-2xl mb-10">
          다채로운 책의 세계를 탐험하고, 당신만의 독서 팔레트를 만들어보세요.
        </p>
        <button @click="() => document.getElementById('section-2')?.scrollIntoView({ behavior: 'smooth' })"
                class="px-8 py-3 bg-emerald-500 text-white font-semibold rounded-lg shadow-md hover:bg-emerald-600 transition-colors duration-300 text-lg">
          시작하기
        </button>
      </section>

      <section id="section-2" class="min-h-screen py-20 px-4 md:px-8 bg-white">
        <h2 class="text-4xl font-bold text-center mb-16 text-gray-800">카테고리 둘러보기</h2>
        <CategorySection />
      </section>

      <section id="section-3" class="min-h-screen py-20 px-4 md:px-8 bg-slate-50">
        <h2 class="text-4xl font-bold text-center mb-16 text-gray-800">추천 도서</h2>
        <BookRecommendSection />
      </section>

      <section id="section-4" class="min-h-screen py-20 px-4 md:px-8 bg-white">
        <h2 class="text-4xl font-bold text-center mb-16 text-gray-800">커뮤니티</h2>
        <CommunitySection />
      </section>
    </template>
    
    <!-- 라우팅된 컴포넌트가 여기에 표시됨 (예: 로그인, 회원가입 페이지) -->
    <router-view v-else />

  </main>

  <transition
    enter-active-class="transition duration-300 ease-out"
    enter-from-class="opacity-0 translate-y-4"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition duration-200 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 translate-y-4"
  >
    <button
      v-show="showScrollTop && isHomePage" <!-- isHomePage 조건 추가 -->
      @click="scrollToTop"
      aria-label="Scroll to top"
      class="fixed bottom-8 right-8 z-50 bg-emerald-500 text-white w-12 h-12 rounded-full shadow-xl flex items-center justify-center hover:bg-emerald-600 transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7 7 7" />
      </svg>
    </button>
  </transition>
</template>

<style scoped>
section {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#section-1 {
  /* pt-16은 main 태그로 옮겨졌으므로, 여기서는 추가 패딩만 고려 */
  padding-top: 0; /* 이미 main에서 pt-16 적용 */
  padding-bottom: 4rem;
}

#section-2, #section-3, #section-4 {
   padding-top: 5rem;
   padding-bottom: 5rem;
   justify-content: flex-start;
}

/* router-view를 위한 스타일 (필요한 경우) */
/* 예: router-view가 main의 pt-16을 상속받도록 하거나, 자체 패딩을 가지도록 설정 */
/* main > router-view { padding-top: 0; } */ 
/* 또는 LoginView/RegisterView 자체에서 min-h-screen과 패딩 관리 */
</style>
