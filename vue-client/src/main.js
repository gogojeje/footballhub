import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://192.168.0.13:5000/';  // Flask API 서버 주소

createApp(App)
  .use(router)
  .mount('#app');


const instance = axios.create({
   baseURL: "http://192.168.0.13:5000/",
   timeout: 1000,
});

export default instance;