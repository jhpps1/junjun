import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Django 서버 주소/포트에 맞게 수정
  withCredentials: true, // 필요시(CSRF 등)
})

export default api
