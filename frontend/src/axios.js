import axios from 'axios'
import { useUserStore } from './stores/user'

const instance = axios.create()

instance.interceptors.request.use(config => {
  const access = localStorage.getItem('access')
  if (access) {
    config.headers.Authorization = `Bearer ${access}`
  }
  return config
})

let isRefreshing = false
let refreshSubscribers = []

function onRefreshed(token) {
  refreshSubscribers.forEach(cb => cb(token))
  refreshSubscribers = []
}

function addRefreshSubscriber(cb) {
  refreshSubscribers.push(cb)
}

instance.interceptors.response.use(
  response => response,
  async error => {
    const userStore = useUserStore()
    const originalRequest = error.config
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      const refresh = localStorage.getItem('refresh')
      if (refresh) {
        if (isRefreshing) {
          // 이미 refresh 중이면, 새 토큰 발급 후 재시도 대기
          return new Promise((resolve, reject) => {
            addRefreshSubscriber(token => {
              if (token) {
                originalRequest.headers.Authorization = `Bearer ${token}`
                resolve(instance(originalRequest))
              } else {
                userStore.logout()
                reject(error)
              }
            })
          })
        }
        originalRequest._retry = true
        isRefreshing = true
        try {
          const res = await axios.post('/api/users/token/refresh/', { refresh })
          const newAccess = res.data.access
          localStorage.setItem('access', newAccess)
          onRefreshed(newAccess)
          isRefreshing = false
          originalRequest.headers.Authorization = `Bearer ${newAccess}`
          return instance(originalRequest)
        } catch (e) {
          isRefreshing = false
          onRefreshed(null)
          userStore.logout()
          return Promise.reject(e)
        }
      } else {
        userStore.logout()
      }
    }
    return Promise.reject(error)
  }
)

export default instance
