// src/api/book.js
import axios from 'axios'
const API_BASE_URL = 'http://localhost:8000/api'

// 인기 도서 목록 불러오기
export function fetchPopularBooks() {
  return axios.get(`${API_BASE_URL}/books/popular/`)
}

export function fetchRecommendedBooksByColor(userId) {
  return axios.get(`${API_BASE_URL}/books/recommend/${userId}/`)
}