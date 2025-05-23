import { defineStore } from 'pinia'
import axios from 'axios'
import { API_URL, FIXTURE_PATH } from '../consts'

interface Category {
  pk: number
  name: string
  color: string
  image?: string | null
  cid_list?: number[]
}

interface Book {
  pk: number
  title: string
  author: string
  publisher: string
  pub_date: string
  description: string
  isbn: string
  cover_image: string
  category: Category
  price: number
  rating?: number
}

interface Review {
  pk: number
  book: number
  user: string
  content: string
  emotion_score: number
  created_at: string
  updated_at: string
}

export const useBookStore = defineStore('book', {
  state: () => ({
    categories: [] as Category[],
    books: [] as Book[],
    recentReviews: [] as Review[],
    currentBook: null as Book | null,
    loading: false,
    error: null as string | null,
  }),

  getters: {    
    booksByCategory: (state) => (categoryPk: number) => {
      return state.books.filter(book => book.category.pk === categoryPk)
    },
    getPopularBooks: (state) => {
      // 랜덤으로 평점이 높은 4개의 책을 반환 (실제로는 평점을 부여하는 로직이 필요)
      const booksWithRating = [...state.books].map(book => ({
        ...book,
        rating: book.rating || Math.random() * 5 // 기존 평점이 없으면 랜덤 생성
      }));
      return booksWithRating.sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 4);
    },
    getAverageEmotionScore: (state) => {
      if (state.recentReviews.length === 0) return 0
      const sum = state.recentReviews.reduce((acc, review) => acc + review.emotion_score, 0)
      return sum / state.recentReviews.length
    },
  },  
  actions: {
    async loadFixtureData() {
      try {
        this.loading = true
        this.error = null
        
        // 카테고리 데이터 로드 - fixture 폴더에서 JSON 파일을 가져옴
        console.log('Loading categories from:', `${FIXTURE_PATH}/category_groups_with_color.json`)
        const categoriesResponse = await fetch(`${FIXTURE_PATH}/category_groups_with_color.json`)
        
        if (!categoriesResponse.ok) {
          throw new Error(`카테고리 데이터 로드 실패 (${categoriesResponse.status}): ${categoriesResponse.statusText}`)
        }
        
        const categoryData = await categoriesResponse.json()
        
        if (Array.isArray(categoryData)) {
          this.categories = categoryData.map((item: any) => ({
            pk: item.pk,
            name: item.name,
            color: item.color || '#CCCCCC', // 기본 색상 설정
            cid_list: item.cid_list,
            image: item.image || null // 이미지 필드 추가
          }))
          console.log('카테고리 데이터 로드 완료:', this.categories.length, '개')
        } else {
          console.error('카테고리 데이터 형식이 올바르지 않습니다:', categoryData)
          throw new Error('카테고리 데이터 형식이 올바르지 않습니다')
        }

        // 책 데이터 로드 - 백엔드 API를 통해 fixture 데이터를 가져옴
        try {
          const booksResponse = await axios.get(`${API_URL}/books/fixture/`)
          
          if (Array.isArray(booksResponse.data)) {
            this.books = booksResponse.data.map((item: any) => {
              // Django fixture 포맷인 경우 (model, pk, fields 구조)
              const fields = item.fields || item
              const categoryName = fields.category_name || fields.category || 'Unknown'
              const category = this.categories.find(cat => cat.name === categoryName)
              
              return {
                pk: item.pk || fields.id || Math.random(), // pk가 없으면 id 또는 랜덤값 사용
                title: fields.title || 'Unknown Title',
                author: fields.author || 'Unknown Author',
                publisher: fields.publisher || 'Unknown Publisher',
                pub_date: fields.pub_date || new Date().toISOString().split('T')[0],
                description: fields.description || '설명이 없습니다.',
                isbn: fields.isbn || '0000000000000',
                cover_image: fields.cover_image || 'https://placehold.co/200x300/e9e9e9/5d5d5d?text=No+Cover',
                price: fields.price || 0,
                category: category || { pk: -1, name: 'Unknown', color: '#808080' },
                rating: fields.rating || (Math.floor(Math.random() * 50) / 10 + 3) // 기본 평점 설정
              }
            })
            console.log('책 데이터 로드 완료:', this.books.length, '개')
          } else {
            console.error('책 데이터 형식이 올바르지 않습니다:', booksResponse.data)
            throw new Error('책 데이터 형식이 올바르지 않습니다')
          }
        } catch (error: any) {
          console.error('백엔드 API에서 책 데이터를 가져오는 데 실패했습니다:', error)
          // 백엔드 API 실패 시 임시 데이터 사용 (선택적)
          this.books = [
            { pk: 1, title: '임시 책 1', author: '저자 1', publisher: '출판사', pub_date: '2023-01-01', description: '설명', isbn: '123456789', cover_image: 'https://placehold.co/200x300/e9e9e9/5d5d5d?text=Book+1', price: 10000, category: this.categories[0] || { pk: 1, name: 'Fiction', color: '#FFD700' }, rating: 4.5 },
            { pk: 2, title: '임시 책 2', author: '저자 2', publisher: '출판사', pub_date: '2023-02-01', description: '설명', isbn: '987654321', cover_image: 'https://placehold.co/200x300/e9e9e9/5d5d5d?text=Book+2', price: 12000, category: this.categories[1] || { pk: 2, name: 'Science', color: '#ADD8E6' }, rating: 4.0 }
          ]
          console.log('임시 책 데이터 사용 (백엔드 API 실패)')
        }

        this.error = null
      } catch (error: any) {
        console.error('fixture 데이터 로드 중 오류 발생:', error)
        this.error = error.message || '데이터를 불러오는데 실패했습니다.'
        // 카테고리와 책 데이터를 빈 배열로 초기화
        this.categories = []
        this.books = []
      } finally {
        this.loading = false
      }
    },

    // API 연동 시 사용할 메서드들
    async fetchCategories() {
      try {
        this.loading = true
        const response = await axios.get(`${API_URL}/categories/`)
        this.categories = response.data.results
      } catch (error: any) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },    async fetchBooks(categoryPk?: number) {
      try {
        this.loading = true
        const params = categoryPk ? { category: categoryPk } : {}
        const response = await axios.get(`${API_URL}/books/`, { params })
        this.books = response.data.results
      } catch (error: any) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },    async fetchBookDetails(bookPk: number) {
      try {
        this.loading = true
        const response = await axios.get(`${API_URL}/books/${bookPk}/`)
        this.currentBook = response.data
      } catch (error: any) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },

    async fetchRecentReviews() {
      try {
        const response = await axios.get(`${API_URL}/reviews/`, {
          params: { ordering: '-created_at', limit: 5 }
        })
        this.recentReviews = response.data.results
      } catch (error: any) {
        this.error = error.message
      }
    },    async submitReview(bookPk: number, content: string) {
      try {
        this.loading = true
        await axios.post(`${API_URL}/reviews/`, {
          book: bookPk,
          content
        })
        await this.fetchRecentReviews()
      } catch (error: any) {
        this.error = error.message
        throw error
      } finally {
        this.loading = false
      }
    },  },
})
