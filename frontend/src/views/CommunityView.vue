<template>
  <div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2>커뮤니티</h2>
      <button class="btn btn-success">글쓰기</button>
    </div>
    <!-- 게시글 리스트 -->
    <div class="card mb-3" v-for="n in 3" :key="n">
      <div class="card-body">
        <h5 class="card-title">게시글 제목 {{ n }}</h5>
        <p class="card-text">게시글 내용 프리뷰...</p>
        <span class="badge bg-secondary">작성자</span>
        <span class="text-muted ms-2">2024-05-27</span>
      </div>
    </div>
  </div>
</template>
