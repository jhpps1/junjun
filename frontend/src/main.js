import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'

// 1. 앱 생성
const app = createApp(App)

// 2. Pinia 생성 및 플러그인 등록
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

// 3. 앱 마운트
app.mount('#app')
