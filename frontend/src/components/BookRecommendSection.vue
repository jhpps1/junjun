<template>
  <!-- 1. 컬러 원형 시각화 -->
  <div class="flex flex-col items-center my-10">
    <div class="flex items-center gap-8">
      <!-- 내 프로필 컬러 -->
      <div class="flex flex-col items-center">
        <div class="w-12 h-12 rounded-full border-4" :style="{ backgroundColor: myColor }"></div>
        <span class="text-xs mt-1 font-bold text-gray-700">나</span>
      </div>
      <!-- 비슷한 유저 컬러 -->
      <div class="flex flex-col items-center cursor-pointer" @click="showUser('similar')">
        <div class="w-10 h-10 rounded-full border-2" :style="{ backgroundColor: similarUser?.profile_color || '#eee' }"></div>
        <span class="text-xs mt-1 text-indigo-700 font-bold">{{ similarUser?.username || '유사유저' }}</span>
      </div>
      <!-- 반대 유저 컬러 -->
      <div class="flex flex-col items-center cursor-pointer" @click="showUser('opposite')">
        <div class="w-10 h-10 rounded-full border-2" :style="{ backgroundColor: oppositeUser?.profile_color || '#eee' }"></div>
        <span class="text-xs mt-1 text-pink-600 font-bold">{{ oppositeUser?.username || '반대유저' }}</span>
      </div>
    </div>
    <!-- 팝업 -->
    <UserBookPopup
      v-if="popupUser"
      :user="popupUser"
      @close="popupUser = null"
    />
  </div>

  <!-- 2. 추천 리스트: 비슷한 유저 -->
  <div class="mb-12">
    <div class="flex items-center justify-center gap-4 mb-2">
      <div
        v-if="similarUser"
        class="w-7 h-7 rounded-full border-2"
        :style="{ backgroundColor: similarUser.profile_color, borderColor: similarUser.profile_color }"
      ></div>
      <span class="font-bold text-indigo-700">
        {{ similarUser?.username || '유사 유저' }}
      </span>
      <span class="ml-2 text-gray-500">님이 많이 찜한 책</span>
    </div>
    <div class="flex flex-wrap gap-8 justify-center">
      <div
        v-for="book in similarBooks"
        :key="'s-' + book.id"
        class="w-64 min-h-[180px] p-6 rounded-2xl border-4 shadow-md flex flex-col justify-between
               hover:shadow-xl hover:-translate-y-2 transition relative"
        :style="{ borderColor: book.color, background: '#fff' }"
      >
        <div>
          <div class="text-xl font-bold mb-1 truncate">{{ book.title }}</div>
          <div class="text-sm text-gray-600 mb-2 truncate">{{ book.author }}</div>
        </div>
        <span class="mt-2 px-3 py-1 rounded-full text-xs font-semibold"
              :style="{ backgroundColor: book.color, color: '#fff' }">
          {{ book.category }}
        </span>
        <!-- 찜/읽음 버튼 -->
        <div class="absolute top-3 right-4 flex flex-col gap-2 items-end">
          <button
            class="text-2xl hover:scale-125 transition"
            :style="{ color: book.isLiked ? book.color : '#bbb' }"
            @click="toggleLike(book, 'similar')"
          >★</button>
          <button
            class="text-xs px-3 py-1 rounded-full border"
            :style="{
              color: book.isRead ? book.color : '#bbb',
              borderColor: book.color,
              background: book.isRead ? '#f0f0f0' : '#fff'
            }"
            @click="toggleRead(book, 'similar')"
          >읽음</button>
        </div>
      </div>
      <span v-if="!similarBooks.length" class="text-gray-400">추천 책이 없습니다.</span>
    </div>
  </div>

  <!-- 3. 추천 리스트: 반대 유저 -->
  <div>
    <div class="flex items-center justify-center gap-4 mb-2">
      <div
        v-if="oppositeUser"
        class="w-7 h-7 rounded-full border-2"
        :style="{ backgroundColor: oppositeUser.profile_color, borderColor: oppositeUser.profile_color }"
      ></div>
      <span class="font-bold text-pink-600">
        {{ oppositeUser?.username || '반대 유저' }}
      </span>
      <span class="ml-2 text-gray-500">님이 많이 찜한 책</span>
    </div>
    <div class="flex flex-wrap gap-8 justify-center">
      <div
        v-for="book in oppositeBooks"
        :key="'o-' + book.id"
        class="w-64 min-h-[180px] p-6 rounded-2xl border-4 shadow-md flex flex-col justify-between
               hover:shadow-xl hover:-translate-y-2 transition relative"
        :style="{ borderColor: book.color, background: '#fff' }"
      >
        <div>
          <div class="text-xl font-bold mb-1 truncate">{{ book.title }}</div>
          <div class="text-sm text-gray-600 mb-2 truncate">{{ book.author }}</div>
        </div>
        <span class="mt-2 px-3 py-1 rounded-full text-xs font-semibold"
              :style="{ backgroundColor: book.color, color: '#fff' }">
          {{ book.category }}
        </span>
        <div class="absolute top-3 right-4 flex flex-col gap-2 items-end">
          <button
            class="text-2xl hover:scale-125 transition"
            :style="{ color: book.isLiked ? book.color : '#bbb' }"
            @click="toggleLike(book, 'opposite')"
          >★</button>
          <button
            class="text-xs px-3 py-1 rounded-full border"
            :style="{
              color: book.isRead ? book.color : '#bbb',
              borderColor: book.color,
              background: book.isRead ? '#f0f0f0' : '#fff'
            }"
            @click="toggleRead(book, 'opposite')"
          >읽음</button>
        </div>
      </div>
      <span v-if="!oppositeBooks.length" class="text-gray-400">추천 책이 없습니다.</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'
import UserBookPopup from './UserBookPopup.vue'

const similarBooks = ref([])
const oppositeBooks = ref([])
const similarUser = ref(null)
const oppositeUser = ref(null)
const myColor = ref('#cccccc')
const popupUser = ref(null)

// 현재 로그인 유저의 찜/읽음 목록
const likes = ref([])
const reads = ref([])

function showUser(type) {
  if (type === 'similar' && similarUser.value) popupUser.value = similarUser.value
  if (type === 'opposite' && oppositeUser.value) popupUser.value = oppositeUser.value
}

async function fetchAll() {
  // 내 프로필 컬러
  const resMe = await axios.get('/api/users/me/')
  myColor.value = resMe.data.profile_color || '#cccccc'

  // 추천 유저와 책
  const res = await axios.get('/api/books/recommend/')
  similarBooks.value = res.data.similar || []
  oppositeBooks.value = res.data.opposite || []
  similarUser.value = res.data.similar_user || null
  oppositeUser.value = res.data.opposite_user || null

  // 내 찜/읽음
  const resLikes = await axios.get('/api/relations/?status=like')
  likes.value = resLikes.data.map(rel => rel.book)
  const resReads = await axios.get('/api/relations/?status=read')
  reads.value = resReads.data.map(rel => rel.book)

  // 추천 책들에 상태 부여
  for (const arr of [similarBooks.value, oppositeBooks.value]) {
    for (const book of arr) {
      book.isLiked = likes.value.includes(book.id)
      book.isRead = reads.value.includes(book.id)
    }
  }
}

onMounted(fetchAll)

async function toggleLike(book, type) {
  if (book.isLiked) {
    const res = await axios.get('/api/relations/?status=like')
    const rel = res.data.find(r => r.book === book.id)
    if (rel) await axios.delete(`/api/relations/${rel.id}/`)
  } else {
    await axios.post('/api/relations/', { book: book.id, status: 'like' })
  }
  await fetchAll()
}

async function toggleRead(book, type) {
  if (book.isRead) {
    const res = await axios.get('/api/relations/?status=read')
    const rel = res.data.find(r => r.book === book.id)
    if (rel) await axios.delete(`/api/relations/${rel.id}/`)
  } else {
    await axios.post('/api/relations/', { book: book.id, status: 'read' })
  }
  await fetchAll()
}
</script>
