<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top shadow-sm">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#">BookPalette</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="#popular" @click.prevent="scrollTo('popular')">인기도서</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#recommend" @click.prevent="scrollTo('recommend')">추천도서</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#category" @click.prevent="scrollTo('category')">카테고리</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#community" @click.prevent="scrollTo('community')">커뮤니티</a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/login" class="nav-link">로그인</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/register" class="nav-link">회원가입</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useUserStore } from '@/store/user'
import { useRouter } from 'vue-router'
const userStore = useUserStore()
const router = useRouter()

function handleLogout() {
  userStore.logout()
  router.push('/login')
}
function scrollTo(section) {
  const el = document.getElementById(section)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
</script>
