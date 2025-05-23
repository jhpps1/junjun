<template>
  <form @submit.prevent="save" class="bg-white p-8 rounded-xl shadow max-w-lg mx-auto my-8 flex flex-col gap-4">
    <div class="flex items-center gap-4">
      <div class="w-12 h-12 rounded-full" :style="{ backgroundColor: user.profile_color || '#eee' }"></div>
      <div class="font-bold">{{ user.username }}</div>
    </div>
    <input v-model="profileColor" type="color" class="w-20 h-10 border rounded" />
    <button type="submit" class="px-6 py-2 bg-indigo-500 text-white font-bold rounded">색상 변경</button>
    <div v-if="success" class="text-green-500 mt-2">변경 완료!</div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios.js'

const user = ref({})
const profileColor = ref('#eeeeee')
const success = ref(false)

onMounted(async () => {
  const res = await axios.get('/api/users/me/')
  user.value = res.data
  profileColor.value = res.data.profile_color || '#eeeeee'
})

async function save() {
  await axios.put('/api/users/me/', { profile_color: profileColor.value })
  success.value = true
  user.value.profile_color = profileColor.value
}
</script>
