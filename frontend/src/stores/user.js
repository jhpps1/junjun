import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from '../axios'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  async function fetchMe() {
    try {
      const res = await axios.get('/api/users/me/')
      user.value = res.data
    } catch {
      user.value = null
    }
  }

  function setUser(data) {
    user.value = data
  }

  function logout() {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    user.value = null
  }

  return { user, fetchMe, setUser, logout }
}, {
  persist: true // 자동 localStorage 동기화
})
