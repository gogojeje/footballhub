<template>
  <div>
    <h1>경기 일정</h1>

        <!-- 마이 팀 정보 표시 -->
        <div v-if="selectedTeam">
      <div class="my-3"><h2>마이 팀: {{ getTeamName(selectedTeam) }}</h2></div>
    </div>

    
    <div class="table-responsive">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>날짜</th>
            <th>시간</th>
            <th>대회</th>
            <th>라운드</th>
            <th>홈팀</th>
            <th>어웨이팀</th>
            <th>스트리밍</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="match in filteredMatches" :key="match[0]">
            <td>{{ match[2] }}</td>
            <td>{{ match[3] }}</td>
            <td>{{ match[4] }}</td>
            <td>{{ match[1] }}</td>
            <td>{{ getTeamName(match[8]) }}</td>
            <td>{{ getTeamName(match[9]) }}</td>
            <td>
              <div class="btn-group" role="group">
                <button @click="openExternalPopup('https://www.spotvnow.co.kr/')" class="btn btn-info">스포티비</button>
                <button @click="openExternalPopup('https://www.coupangplay.com/home')" class="btn btn-primary">쿠팡플레이</button>
                <button @click="openExternalPopup('https://www.tving.com/onboarding')" class="btn btn-danger">티빙</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      matches: [],
      teams: [],
      selectedTeam: '' // 추가: 선택한 마이팀 저장
    };
  },
  mounted() {
    this.fetchData();
  },
  computed: {
    filteredMatches() {
      if (!this.selectedTeam) {
        return this.matches;
      }
      return this.matches.filter(match => match[8] === this.selectedTeam || match[9] === this.selectedTeam);
    }
  },
  methods: {
    fetchData() {
      axios.get('http://192.168.0.13:5000/api/get_schedule_and_teams')
        .then(response => {
          this.matches = response.data.matches;
          this.teams = response.data.teams;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    getTeamName(teamId) {
      const team = this.teams.find(team => team[0] === teamId);
      return team ? team[1] : 'Unknown Team';
    },
    openExternalPopup(url) {
      const popupWindow = window.open(url, '_blank', 'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=1600,height=900');
      if (!popupWindow) {
        alert('팝업이 차단되었습니다. 이 웹사이트에서 팝업을 허용해주세요.');
      }
    }
  }
};
</script>

<style>
.table-responsive {
  overflow-x: auto;
}

.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 1rem;
  background-color: transparent;
}

.table th,
.table td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table thead th {
  vertical-align: bottom;
  border-bottom: 2px solid #dee2e6;
}

.table tbody + tbody {
  border-top: 2px solid #dee2e6;
}

.table-sm th,
.table-sm td {
  padding: 0.3rem;
}

/* 버튼 그룹 스타일 */
.btn-group {
  display: flex;
  gap: 10px;
}

/* 버튼 스타일 */
.btn {
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.25rem;
}

.btn-info {
  color: #fff;
  background-color: #17a2b8;
  border-color: #17a2b8;
}

.btn-primary {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}

.btn-danger {
  color: #fff;
  background-color: #dc3545;
  border-color: #dc3545;
}

/* 버튼 호버 효과 */
.btn:hover {
  filter: brightness(90%);
}
</style>
