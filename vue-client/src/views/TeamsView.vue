<template>
  <div class="team-selection">
    <h1>좋아하는 팀을 선택하세요.</h1>

    <!-- League Selection Dropdown -->
    <div class="dropdown">
      <label for="league-dropdown" class="dropdown-label">리그 선택</label>
      <select
        id="league-dropdown"
        class="form-select"
        v-model="selectedLeague"
        @change="filterTeamsByLeague"
      >
        <option value="">모든 리그</option>
        <option v-for="league in uniqueLeagues" :key="league">{{ league }}</option>
      </select>
    </div>

    <!-- Team Selection Dropdown -->
    <div class="dropdown">
      <label for="team-dropdown" class="dropdown-label">팀 선택</label>
      <select id="team-dropdown" class="form-select" v-model="selectedTeam">
        <option value="">모든 팀</option>
        <option v-for="team in filteredTeams" :key="team.id">{{ team.name }}</option>
      </select>
    </div>

    <button @click="handleSetPreferredTeam" class="btn btn-primary">마이 팀 설정하기</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TeamsView',
  props: ['teamSelected'],
  data() {
    return {
      teams: [],
      selectedLeague: '', // 선택한 리그 이름
      selectedTeam: '',   // 선택한 팀 이름
    };
  },
  computed: {
    uniqueLeagues() {
      const leagues = new Set();
      this.teams.forEach(team => leagues.add(team.league));
      return Array.from(leagues);
    },
    filteredTeams() {
      let teamsToShow = this.teams;
      if (this.selectedLeague) {
        teamsToShow = teamsToShow.filter(team => team.league === this.selectedLeague);
      }
      return teamsToShow;
    }
  },
  created() {
    this.fetchTeams();
  },
  methods: {
    async fetchTeams() {
      try {
        const response = await axios.get('/api/teams/');
        this.teams = response.data;
      } catch (error) {
        console.error('An error occurred while fetching teams:', error);
      }
    },




    filterTeamsByLeague() {
      this.selectedTeam = ''; // 팀 선택 초기화
    },


handleSetPreferredTeam() {
  if (this.selectedTeam) {
    this.$emit('teamSelected', this.selectedTeam); // 선택한 팀을 이벤트로 전달
  } else {
    alert('Please select a team before setting as preferred.');
  }
}
}};
</script>

<style scoped>
.team-selection {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.dropdown {
  margin-bottom: 20px;
}

.dropdown-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>