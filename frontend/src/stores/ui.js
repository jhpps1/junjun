import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const isDark = ref(localStorage.getItem('isDark') === 'true')

  function toggleDark() {
    isDark.value = !isDark.value
    localStorage.setItem('isDark', isDark.value)
    document.documentElement.classList.toggle('dark', isDark.value)
  }

  // 앱 시작 시 다크모드 적용
  if (isDark.value) {
    document.documentElement.classList.add('dark')
  }

  return { isDark, toggleDark }
})
