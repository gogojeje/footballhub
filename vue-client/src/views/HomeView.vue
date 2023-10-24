<template>
  <div class="container">
    <h1 class="my-4">
      <a href="/" style="text-decoration: none; color: inherit;">FOOTBALL HUB®</a>
    </h1>

    <!-- 로그인하지 않은 상태 -->
    <div v-if="!isLoggedIn">
      <div class="card my-4">
        <div class="card-body">
          <p class="card-text">올바른 축구중계 플랫폼, 풋볼허브</p>
          <form @submit.prevent="login">
            <div class="mb-3">
              <label for="userid" class="form-label">아이디</label>
              <input v-model="userid" type="text" id="userid" class="form-control" required>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">패스워드</label>
              <input v-model="password" type="password" id="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary me-2">로그인</button>
            <button @click="goToSignUp" class="btn btn-secondary">회원가입</button>
          </form>
          <p v-if="message" class="mt-2">{{ message }}</p>
        </div>
      </div>
    </div>

    <!-- 로그인한 상태 -->
    <div v-if="isLoggedIn">
      <div class="card my-4">
        <div class="card-body">
          <p class="card-text">풋볼허브에 오신 걸 환영합니다, {{ userid }}!</p>
          <button @click="openTeamsModal" class="btn btn-primary me-2">마이 팀</button>
          <button class="btn btn-secondary" @click="logout">로그아웃</button>
          <div class="my-3"><h2>마이 팀: {{ selectedTeam }}</h2></div>
        </div>
      </div>
    </div>

    <!-- 일정 뷰 -->
  
    <div class="d-flex justify-content-between mb-4">
      <button @click="toggleViewSchedule('전체')" class="btn btn-primary">전체 일정</button>
      <button @click="toggleViewSchedule('마이')" class="btn btn-primary">마이 팀 일정</button>
    </div>

    <ScheduleView v-if="isViewingSchedule" :matches="filteredMatches" :teams="teams" />


    <!-- Teams 모달 창 -->
    <div v-if="showTeamsModal" class="modal fade show" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">마이 팀</h5>
            <button type="button" class="btn-close" @click="closeTeamsModal"></button>
          </div>
          <div class="modal-body">
            <TeamsView @teamSelected="handleTeamSelected" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TeamsView from '@/views/teamsview.vue';
import ScheduleView from '@/views/scheduleview.vue';

export default {
  name: 'HomeView',
  components: {
    TeamsView,
    ScheduleView,
  },

  created() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const userid = localStorage.getItem('userid');
    if (isLoggedIn && userid) {
      this.isLoggedIn = true;
    this.userid = userid;
  }

  // 세션에서 마이팀 정보를 로드
  const selectedTeam = sessionStorage.getItem('selectedTeam');
  if (selectedTeam) {
    this.selectedTeam = selectedTeam;
  }

  // 홈 화면이 로드될 때 스케줄을 표시하도록 호출
  this.toggleViewSchedule('전체');
},

  data() {
    return {
      userid: '',
      password: '',
      isLoggedIn: false,
      showTeamsModal: false,
      selectedTeam: '',
      message: '',
      isViewingSchedule: false,
      filteredMatches: [],
      teams: [], // 팀 정보를 저장할 배열
    };
  },


  methods: {
    async login() {
      try {
        const response = await axios.post('http://192.168.0.13:5000/api/login', {
      userid: this.userid,
      password: this.password
    });

    if (response.data === 'Login successful') {
      // 로그인 성공 시 로컬 스토리지에 로그인 상태 저장
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('userid', this.userid);

      // 마이팀 선택 정보를 세션에 저장
      sessionStorage.setItem('selectedTeam', this.selectedTeam);

      this.message = '';
      this.isLoggedIn = true;
    } else {
      this.message = '로그인 실패. 정확한 아이디와 비밀번호를 입력해주세요.';
    }
  } catch (error) {
    console.error('An error occurred while logging in:', error);
    this.message = 'An error occurred while logging in';
  }
},





    toggleViewSchedule(type) {
  this.isViewingSchedule = true; // 항상 일정을 표시

  if (type === '마이') {
    if (!this.selectedTeam) {
      this.filteredMatches = []; // 선택된 팀이 없을 경우 일정을 지웁니다.
    } else {
      this.filteredMatches = this.matches.filter(match => {
        const homeTeamId = match[8];
        const awayTeamId = match[9];
        return homeTeamId === this.selectedTeam || awayTeamId === this.selectedTeam;
      });
    }
  } else {
    this.filteredMatches = this.matches; // '전체' 버튼을 누르면 모든 일정을 표시합니다.
  }
},




  


    openExternalPopup(url) {
  const popupWindow = window.open(url, '_blank', 'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=1600,height=900');
  if (!popupWindow) {
    alert('팝업이 차단되었습니다. 이 웹사이트에서 팝업을 허용해주세요.');
  }
},

 

    goToSignUp() {
    // "Sign Up" 버튼을 눌렀을 때의 동작
    // 예를 들어, 새로운 페이지로 이동하거나 모달 창을 열 수 있음
    // 여기서는 새로운 페이지로 라우팅하는 예시를 보여드립니다.

    // Vue Router를 사용해 회원 가입 페이지로 이동하는 예시:
    this.$router.push('/signup'); // '/signup'은 실제 회원 가입 페이지의 경로로 변경해야 합니다.
    },





    openTeamsModal() {
      this.showTeamsModal = true; // 모달 열기
    },

    closeTeamsModal() {
      this.showTeamsModal = false; // 모달 닫기
    },


    handleTeamSelected(selectedTeam) {
      this.selectedTeam = selectedTeam; // 선택한 팀 저장
      this.showTeamsModal = false; // 모달 닫기
      this.$router.push('/'); // 홈 화면으로 이동
    },




    logout() {
      // 로그아웃 시 로컬 스토리지에서 세션 정보 제거
      localStorage.removeItem('isLoggedIn');
      localStorage.removeItem('userid');

      this.isLoggedIn = false;
    }
  }
};
</script>

<style>
.container {
  padding: 20px;
}

.card {
  margin-bottom: 20px;
}

.table {
  margin-bottom: 20px;
}

.modal {
  display: block;
  background-color: rgba(0, 0, 0, 0.4);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1050;
  overflow: auto;
  padding: 30px;
}

.modal-dialog {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
}

.modal-header .btn-close {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>