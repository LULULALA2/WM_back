![image](https://user-images.githubusercontent.com/71905164/182584327-171cf850-0bd8-4d62-bdec-1ba090eb9b71.png)
# 🚀MakeMigrations
**최종 프로젝트 - MakeMigrations : 태양계이주센터**
딥페이크를 이용하여 움직이는 사진을 생성, 지구 밖 행성으로 이주한 사람들의 시민권을 만들어주는 웹사이트

<br>

# ⭐Intro
* 다른 행성들로 이주해서 생활한다는 컨셉의 커뮤니티
* 딥페이크를 이용해서 사진을 움직이게 만들어줌
* 커뮤니티 기능 및 마이 페이지에서 방 꾸미는 기능 등
* S.A : <a href="https://cold-charcoal.tistory.com/118">블로그로 이동(☞ﾟヮﾟ)☞</a>

<br>

# 🪐Project

### 프로젝트 기획

* 시연영상 : <a href="https://cold-charcoal.tistory.com/143">영상 보러 가기(☞ﾟヮﾟ)☞</a>
* 원본 팀 깃허브 : <a href="https://github.com/cmjcum/WM_back">https://github.com/cmjcum/WM_back</a>
* Frontend Repository : <a href="https://github.com/cmjcum/WM_front"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* 프로젝트 기간 : 2022.07.07 ~ 2022.08.16

<br>

### 핵심기능

* JWT를 이용한 로그인
* 딥페이크를 통한 움직이는 사진 생성
* AWS S3에 이미지 저장
* 게시판 페이지네이션
* 바닐라 JS로 구현한 방 꾸미기 기능

<br>

### ✔ 담당 역할

* 회원가입/로그인 페이지 제작
* AWS(S3, Cloudfront) 프론트엔드 배포, CICD(git actions)
* simple JWT token을 이용한 회원가입/로그인 기능
* AWS(EC2, ACM, Route53) docker 백엔드 배포

<br>

### Architecture
![image](https://user-images.githubusercontent.com/71905164/182599471-7262271c-a5b7-4379-8460-0a9b933a51dc.png)

<br>

### API
<a href="https://typingmylife.notion.site/MakeMigrations-API-88de2c1a1ccd457c9059c8b55ee3dc70">노션 페이지로 이동(☞ﾟヮﾟ)☞</a>

<br>

### ERD
![make migrations (6)](https://user-images.githubusercontent.com/71905164/182602214-7d8cf839-76d6-4d30-af03-99d5f9481137.png)

<br>

# 🧨TroubleShooting

### 1. python 버전에 따른 패키지 관리자 호환 문제

### 2. pytorch, tensorflow run 명령어로 설치

### 3. bucket 사용시 권한문제 발생

- awscli 가 docker 내부에 설치안되어 있었던 문제

### 4. 프론트 CICD 반영 → 무효화

<br>

# 🛠사용자 피드백

### 1. xss 공격 대비

### 2. index.html로 돌아왔을 때 로그인을 다시해야하는 경우 방지

<br>

# 실행 화면
![1](https://user-images.githubusercontent.com/71905164/182770710-17111bfc-49fc-4740-9eff-d3fce080082e.png)
![2](https://user-images.githubusercontent.com/71905164/182770720-93402217-4e41-4fab-8211-8286668b8fce.png)
![3](https://user-images.githubusercontent.com/71905164/182770729-fe5141ad-01cb-447a-9533-6c18756927c0.png)
![4](https://user-images.githubusercontent.com/71905164/182770747-131cdbec-2304-49d9-b8d8-1d159cb82905.png)

<br>

# 🌠Credit
* 프로젝트에 사용된 모든 가구 벡터는 <a href='https://kr.freepik.com/author/macrovector'>macrovector - kr.freepik.com가 제작함</a>
* <a href="https://www.flaticon.com/free-icons/planet" title="planet icons">Planet icons created by Eucalyp - Flaticon</a>
