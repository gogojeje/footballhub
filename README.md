1.프로젝트 개요
- 기본 정보
     프로젝트명   : 풋볼허브(축구 중계 사이트 플랫폼)
     프로젝트기간 : 2023년 8월 16일 ~ 25일(10일 간)
     디벨로퍼명   : 정용준
     기타         : ChatGPT 3.5 적극 활용 
  
- 주요 특징 및 차별성
주요 축구경기 일정을 간편하게 확인하고, 각 경기의 중계 사이트를 연결해주는 올바른 축구중계 플랫폼

- 사용한 주요 기술
Oracle / Flask SSR / Flask REST / Bootstrap / jQuery / AJAX / CSS / Vue.js / Vue Router 등


2. Table 작업
- 6개 테이블 생성
(LEAGUESANDTOURNAMENTS, TEAMS, MATCHSCHEDULE, MATCHSTREAMING, MEMBERS, PREFERREDTEAMS)


3. PL/SQL 작업
- 각 테이블에 CRUD를 수행하는 PLSQL 패키지 생성, 컬럼별로 UPDATE하는 프로시저 및 패키지 테스트용 PLSQL 코드 포함

  
4. Flask 작업
- 각 기능별 api를 제작하여 구성
- 기능별로 모듈화하여 여러 개의 .py 파일 작성


5. Vue 작업
- Axios, CORS 사용하여 백엔드와 연동
