<template>
  <div class="signup-container">
    <h2>회원가입</h2>
    <form @submit.prevent="signup" class="signup-form">
      <div class="form-group">
        <label for="userid">아이디:</label>
        <input v-model="userid" type="text" id="userid" required>
      </div>
      <div class="form-group">
        <label for="password">비밀번호:</label>
        <input v-model="password" type="password" id="password" required>
      </div>
      <div class="form-group">
        <label for="username">닉네임:</label>
        <input v-model="username" type="text" id="username" required>
      </div>
      <div class="form-group">
        <label for="email">이메일:</label>
        <input v-model="email" type="email" id="email" required>
      </div>

      <div class="form-group">
        <label for="gender">성별:</label>
        <select v-model="gender" id="gender">
          <option value="Male">남성</option>
          <option value="Female">여성</option>
        </select>
      </div>
      <div class="form-group">
        <label for="age">만 나이</label>
        <input v-model="age" type="number" id="age" required>
      </div>
      <div class="form-group">
        <label for="location">지역:</label>
        <input v-model="location" type="text" id="location" required>
      </div>
      <button type="submit" class="btn btn-primary">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userid: '',
      username: '',
      email: '',
      password: '',
      gender: 'Male',
      age: 0,
      location: ''
    };
  },
  methods: {
    async signup() {
      try {
        const response = await axios.post('http://192.168.0.13:5000/api/signup', {
          userid: this.userid,
          username: this.username,
          email: this.email,
          password: this.password,
          gender: this.gender,
          age: this.age,
          location: this.location
        });
        if (response.data === 'Signup successful!') {
          const loginResponse = await axios.post('http://192.168.0.13:5000/api/login', {
            userid: this.userid,
            password: this.password
          });
          if (loginResponse.data === 'Login successful') {
            alert('회원가입 성공!');
            this.$router.push('/');
          } else {
            alert('Signup successful, but login failed. Please login manually.');
          }
        } else {
          alert('Signup failed. Please check your input.');
        }
      } catch (error) {
        console.error('An error occurred while signing up:', error);
      }
    }
  }
};
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"],
input[type="number"],
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

select {
  cursor: pointer;
}

.btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
}

/* Add more styles as needed */
</style>