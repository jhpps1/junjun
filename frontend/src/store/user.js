import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    user: null,
    error: null,
  }),
  persist: true,
  actions: {
    async login(username, password) {
      try {
        const res = await axios.post('http://localhost:8000/api/accounts/login/', { username, password }, { withCredentials: true })
        this.isLoggedIn = true
        this.user = res.data.user
        this.error = null
      } catch (err) {
        this.error = err.response?.data?.detail || '로그인 실패'
        this.isLoggedIn = false
        this.user = null
      }
    },
    async register(username, password) {
      try {
        await axios.post('http://localhost:8000/api/accounts/register/', { username, password })
        this.error = null
        return true
      } catch (err) {
        this.error = err.response?.data?.detail || '회원가입 실패'
        return false
      }
    },
    async logout() {
      await axios.post('http://localhost:8000/api/accounts/logout/', {}, { withCredentials: true })
      this.isLoggedIn = false
      this.user = null
      this.error = null
    }
  }
})
