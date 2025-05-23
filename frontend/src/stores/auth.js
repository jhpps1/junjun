import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'; // axios import

// Django 백엔드 API 기본 URL (환경에 맞게 수정)
const API_URL = 'http://localhost:8000';

export const useAuthStore = defineStore('auth', () => {
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'));
  const token = ref(localStorage.getItem('token') || null); // 토큰 저장
  const router = useRouter();

  const isLoggedIn = computed(() => !!user.value && !!token.value); // 토큰 유무도 확인
  const currentUser = computed(() => user.value);
  const authToken = computed(() => token.value); // 외부에서 토큰 접근 가능하도록

  async function login(username, password) {
    try {
      const response = await axios.post(`${API_URL}/api/auth/login/`, {
        username,
        password,
      });

      const token = response.data.access_token || response.data.key || response.data.token; // 다양한 토큰 키에 대응
      if (!token) {
        throw new Error('Token not found in response');
      }
      user.value = response.data.user;
      token.value = token;

      localStorage.setItem('user', JSON.stringify(response.data.user));
      localStorage.setItem('token', token);

      // API 요청 시 기본 헤더에 토큰 설정
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

      await fetchUser();

      return response.data.user;
    } catch (error) {
      console.error('Login API error:', error.response ? error.response.data : error.message);
      // 서버에서 오는 에러 메시지가 있다면 사용, 없다면 일반 메시지
      const errorMessage = error.response?.data?.non_field_errors?.[0] || 
                           error.response?.data?.detail ||
                           error.message || 
                           '아이디 또는 비밀번호를 확인해주세요.';
      throw new Error(errorMessage);
    }
  }

  async function register(userData) {
    try {
      const response = await axios.post(`${API_URL}/api/users/`, userData);
      // 회원가입 성공 시 별도의 로그인 처리는 하지 않음 (백엔드 설정에 따라 다를 수 있음)
      // 일반적으로 회원가입 후 로그인 페이지로 안내하거나, 자동 로그인 처리 후 토큰을 반환할 수 있음
      // 여기서는 성공 메시지만 반환하고, 로그인 페이지로 리디렉션은 컴포넌트에서 처리
      console.log('Registration successful:', response.data);
      return response.data; // 성공 시 백엔드에서 오는 메시지 또는 데이터 반환
    } catch (error) {
      console.error('Register API error:', error.response ? error.response.data : error.message);
      // 서버에서 오는 에러 메시지가 있다면 사용, 없다면 일반 메시지
      // Django REST framework의 경우 validation error는 보통 필드별로 오거나 non_field_errors로 옴
      let errorMessage = '회원가입에 실패했습니다. 입력 정보를 확인해주세요.';
      if (error.response && error.response.data) {
        const errors = error.response.data;
        if (errors.username) {
          errorMessage = `아이디: ${errors.username.join(', ')}`;
        } else if (errors.email) {
          errorMessage = `이메일: ${errors.email.join(', ')}`;
        } else if (errors.password) {
          errorMessage = `비밀번호: ${errors.password.join(', ')}`;
        } else if (errors.non_field_errors) {
          errorMessage = errors.non_field_errors.join(', ');
        } else if (typeof errors === 'string') {
          errorMessage = errors;
        } else {
          // 기타 예상치 못한 오류 형식
          errorMessage = Object.values(errors).flat().join(' ') || errorMessage;
        }
      }
      throw new Error(errorMessage);
    }
  }

  function logout() {
    user.value = null;
    token.value = null;
    localStorage.removeItem('user');
    localStorage.removeItem('token');
    delete axios.defaults.headers.common['Authorization']; // API 요청 헤더에서 토큰 제거
    
    if (router) {
      router.push('/');
    } else {
      // router가 없는 경우 (예: store가 router보다 먼저 초기화되는 경우)
      // window.location.pathname = '/'; // 직접 경로 변경 (새로고침 발생)
      console.warn('Router instance not available in auth store during logout. Consider redirecting from component.');
    }
  }

  // 페이지 로드 시 토큰이 있다면 사용자 정보 가져오기 시도 (선택적 강화)
  // 이 기능을 사용하려면 앱 초기화 시 (예: main.js 또는 App.vue) 호출해야 합니다.
  async function fetchUser() {
    if (token.value && !user.value) { // 토큰은 있는데 사용자 정보가 없다면
      try {
        // 실제 사용자 정보를 가져올 수 있는 백엔드 엔드포인트로 수정해야 합니다.
        // 예: `${API_URL}/api/auth/user/`
        // 이 엔드포인트는 토큰을 기반으로 현재 사용자 정보를 반환해야 합니다.
        const response = await axios.get(`${API_URL}/api/auth/user/`, { 
          headers: { Authorization: `Bearer ${token.value}` }
        });
        if (response.data) {
            user.value = response.data;
            localStorage.setItem('user', JSON.stringify(response.data));
        } else {
            // 유효한 사용자 데이터를 받지 못한 경우, 토큰이 만료되었거나 잘못된 것일 수 있음
            logout(); // 안전하게 로그아웃 처리
        }
      } catch (error) {
        console.error('Failed to fetch user on load:', error.response ? error.response.data : error.message);
        // 토큰이 유효하지 않을 수 있으므로 로그아웃 처리
        logout(); 
      }
    }
  }

  // 앱 초기화 시 axios 기본 헤더 설정 및 사용자 정보 로드 시도
  if (token.value) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`;
    // fetchUserOnLoad(); // 스토어 정의 시점에 바로 호출하거나, 앱 초기화 로직에서 호출
  }


  return {
    user,
    token, 
    isLoggedIn,
    currentUser,
    authToken,
    login,
    register, // register 함수 추가
    logout,
    fetchUser, // 외부에서 호출할 수 있도록 반환
  };
});
