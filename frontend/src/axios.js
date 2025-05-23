import axios from 'axios'

const instance = axios.create()

instance.interceptors.request.use(config => {
  const access = localStorage.getItem('access')
  if (access) {
    config.headers.Authorization = `Bearer ${access}`
  }
  return config
})

export default instance
