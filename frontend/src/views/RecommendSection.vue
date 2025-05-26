<template>
  <section id="recommend" class="container py-5">
    <h2 class="fw-bold">추천 도서</h2>
    <div class="row mt-4">
      <div class="col-md-5">
        <div class="mb-3">
          <h3 class="fw-bold">{{ books[0].title }}</h3>
          <div class="mb-2 text-muted">{{ books[0].desc }}</div>
        </div>
        <div class="d-flex align-items-center justify-content-center bg-light" style="min-height:200px;">
          <span>책 이미지</span>
        </div>
      </div>
      <div class="col-md-7">
        <div
          v-for="book in books"
          :key="book.id"
          class="mb-4"
        >
          <BookCard :book="book" />
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import BookCard from '@/components/BookCard.vue'
const books = [
  {
    id: 1,
    title: '달의 영휴',
    author: '작가A',
    category: '에세이',
    color: '#a3c1da',
    desc: '감성적인 에세이 샘플입니다.',
    comments: [
      '정말 감동적이었어요!',
      '표현력이 대단합니다.',
      '이 책 덕분에 마음이 따뜻해졌어요.'
    ]
  },
  {
    id: 2,
    title: '마음의 과학',
    author: '작가B',
    category: '심리',
    color: '#f8b195',
    desc: '심리학적 통찰을 담은 책입니다.',
    comments: [
      '쉽게 설명해서 좋았어요.',
      '추천 도서로 딱!',
      '심리학에 처음 입문하는 분께 추천.'
    ]
  },
  {
    id: 3,
    title: '코딩, 너의 의미',
    author: '작가C',
    category: 'IT',
    color: '#6dcff6',
    desc: 'IT 입문자를 위한 감성 도서.',
    comments: [
      '개발자에게 정말 추천!',
      '책이 따뜻한 느낌이에요.',
      '실용적이면서 감성적인 책.'
    ]
  }
]
</script>
