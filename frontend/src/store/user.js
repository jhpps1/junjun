// src/stores/user.js
import { defineStore } from 'pinia'
import api from '@/api/auth'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLogin: false,
    user: null,    // 유저 정보 객체
    loading: false,
  }),
  actions: {
    async fetchMe() {
      this.loading = true
      try {
        const res = await api.get('/accounts/users/me/')
        this.user = res.data
        this.isLogin = !!res.data?.username
      } catch {
        this.user = null
        this.isLogin = false
      } finally {
        this.loading = false
      }
    },
    async login(username, password) {
      await api.post('/accounts/login/', { username, password })
      await this.fetchMe()
    },
    async logout() {
      await api.post('/accounts/logout/')
      this.user = null
      this.isLogin = false
    }
  },
  persist: true
})
