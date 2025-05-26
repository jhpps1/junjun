<template>
  <div class="container py-5">
    <div class="card shadow p-4" style="max-width:500px;margin:auto;">
      <div class="d-flex align-items-center mb-4">
        <div class="rounded-circle bg-secondary" style="width:60px;height:60px;"></div>
        <div class="ms-4">
          <h3>닉네임</h3>
          <span class="badge bg-primary">팔레트 컬러</span>
        </div>
      </div>
      <hr>
      <h5>내가 읽은/찜한 책</h5>
      <ul class="list-group">
        <li class="list-group-item" v-for="n in 2" :key="n">도서 제목 {{ n }}</li>
      </ul>
    </div>
  </div>
</template>
