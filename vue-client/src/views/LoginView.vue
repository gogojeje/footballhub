<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="userid">User ID:</label>
      <input v-model="userid" type="text" id="userid" required>
      <label for="password">Password:</label>
      <input v-model="password" type="password" id="password" required>
      <button type="submit">Login</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userid: '',
      username: '',
      password: '',
      message: ''
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
          this.message = '로그인 성공!';
          // 로그인 성공 시에는 필요한 처리를 수행하세요 (예: 세션 저장 등)
        } else {
          this.message = '로그인 실패. 아이디와 비밀번호를 다시 입력해주세요.';
        }
      } catch (error) {
        console.error('An error occurred while logging in:', error);
        this.message = 'An error occurred while logging in';
      }
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
