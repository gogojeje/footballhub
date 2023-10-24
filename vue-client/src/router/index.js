import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import SignupView from '@/views/SignupView.vue'; // 이 부분에 경로를 정확히 입력해주세요
import TeamsView from '../views/TeamsView.vue';
import ScheduleView from '../views/scheduleview.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      component: LoginView,
    },
    { path: '/signup', 
      component: SignupView 
    }, // signup 경로 등록
    {
      path: '/teams',
      name: 'TeamsView',
      component: TeamsView
    },
       { path: '/matchschedule', 
       component: ScheduleView 
      } // /matchschedule 경로에 ScheduleView 컴포넌트 연결
  ]
})

export default router;
