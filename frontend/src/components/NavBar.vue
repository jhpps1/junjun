<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#">Logo</a>
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#popular">인기도서</a></li>
        <li class="nav-item"><a class="nav-link" href="#category">카테고리</a></li>
        <li class="nav-item"><a class="nav-link" href="#community">커뮤니티</a></li>
        <li class="nav-item"><a class="nav-link" href="#recommend">추천도서</a></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
// 스크롤 이동 함수
function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "start" })
  }
}
</script>

<style>
/* 추가 스타일이 필요한 경우 여기에 작성 */
</style>
