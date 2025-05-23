<template>
  <section class="min-h-[70vh] flex flex-col justify-center items-center text-center bg-gradient-to-br from-pink-100 via-indigo-50 to-cyan-100 relative overflow-hidden">
    <div class="z-10 relative">
      <h1 class="text-5xl md:text-7xl font-extrabold mb-6 tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-pink-400 via-indigo-500 to-cyan-500 drop-shadow">
        Book Palette
      </h1>
      <p class="text-xl md:text-2xl font-semibold mb-8 text-gray-700">
        취향이 색이 되는 독서 커뮤니티
      </p>
      <p class="mb-10 text-lg text-gray-500">
        내가 좋아하는 책과 장르가 감성 컬러로 시각화<br>
        색으로 통하는 추천, 연결, 커뮤니티 경험
      </p>
      <button
        class="px-8 py-3 rounded-full bg-indigo-500 hover:bg-indigo-700 text-white text-lg font-bold shadow transition"
        @click="$emit('scrollTo', 'section-2')"
      >
        시작하기
      </button>
    </div>
    <!-- 장식용 컬러 원 -->
    <div class="absolute -top-32 -left-32 w-80 h-80 rounded-full bg-pink-100 opacity-70 blur-2xl"></div>
    <div class="absolute bottom-0 right-0 w-72 h-72 rounded-full bg-cyan-100 opacity-50 blur-2xl"></div>
  </section>
</template>
