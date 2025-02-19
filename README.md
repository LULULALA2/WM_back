![image](https://user-images.githubusercontent.com/71905164/182584327-171cf850-0bd8-4d62-bdec-1ba090eb9b71.png)

<br>**목차**
<br>[1. 프로젝트 소개](#intro)
<br>[2. 프로젝트 기획 - 시연영상](#프로젝트-기획)
<br>[3. 맡은 역할](#-담당-역할)
<br>[4. 트러블슈팅](#troubleshooting)
<br>[5. 회고](#회고)
<br>

# 🚀MakeMigrations
**최종 프로젝트 - MakeMigrations : 태양계이주센터**
<br>딥페이크를 이용하여 움직이는 사진을 생성, 지구 밖 행성으로 이주한 사람들의 시민권을 만들어주는 웹사이트

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
* Frontend Repository : <a href="https://github.com/cmjcum/WM_front">https://github.com/cmjcum/WM_front</a>
* 프로젝트 기간 : 2022.07.07 ~ 2022.08.16
* 사용자 피드백 반영 기간 : 2022.08.08 ~ 2022.08.11

<br>

### 핵심기능

게시판과 마이홈을 통한 회원들 간의 커뮤니티 기능과 방 꾸미기 기능 구현

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

### 1. python 버전에 따른 호환 문제
① python_alpine 버전을 사용하면서 패키지 관리자를 apt-get 사용

알파인 리눅스는 초경량화된 배포판이므로 docker에서 자주 사용되는 리눅스 이미지인데, 도커와 이미지 버전에 대해서 잘 모르는 상태로 도커를 공부하던 참고영상에서 사용한 버전을 그대로 사용했습니다. 알파인 버전에서는 패키지 관리자로 apk를 사용한다는 사실을 모르고 apt-get을 사용했고 계속 apt-get을 찾을 수 없다는 에러가 발생해서 구글링을 통해 버전에 대한 정보를 얻고 공부해서 수정하게 되었습니다.

② python_alpine 버전에서는 pytorch, tensorflow 사용불가하여 python_buster 버전으로 수정

위에서 알파인 버전으로 Dockerfile 을 작성하여 1차 배포를 마치고 머신러닝을 추가하여 2차 배포를 앞두고 테스트 중이었습니다. pythorh 와 tensorflow 가 들어가면 인식을 못하고 패키지를 설치하지 못하는 에러가 발생했습니다. 알파인 버전에서는 두 패키지를 설치하는 데 필수요소가 들어있지 않아서 설치 불가능 한 것으로 예상을 하고, buster 버전으로 바꾸어주니 에러없이 설치되었습니다. 

<br>

### 2. pytorch, tensorflow run 명령어로 설치
- pytorch, tensorflow는 Requirements.txt 로 한번에 설치하려고 하면 MemoryError 발생
이 패키지를 설치할 때는 캐시를 사용하지 않도록 하는 --no-cache-dir 옵션을 추가해주고, 두 패키지가 용량이 크기때문에 Dockerfile 에서 설치하도록 따로 빼주었습니다.

```python
# Dockerfile
RUN pip install --no-cache-dir tensorflow==2.9.0 
RUN pip install --no-cache-dir torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cpu
```

### 3. bucket 사용시 권한문제 발생
정적파일을 저장하는 bucket은 제 계정을 사용하고 있고, 나머지 기능에서 사용하는 bucket은 기능을 구현한 팀원들 각자의 계정을 사용하고 있어서 권한문제가 발생했습니다. 그래서 EC2 에서 bucket 권한 설정을 해주었는데도 불구하고 계속 bucket을 사용하는 곳에서 권한 사용문제가 떴습니다.

- awscli 가 docker 내부에 설치안되어 있었던 문제
<br>① dockerfile 에 <code>RUN pip install awscli</code> 명령어 추가
<br>docker 내부에 aswcli 설치
<br>② docker-compose.yml 에서 web container 의 volume 설정에 aws 권한인증 저장 폴더 위치를 추가
<br><code>/home/ubuntu/.aws/:/root/.aws/:ro</code>
<br>

### 4. 프론트 CICD 한 내용이 바로 반영이 안되는 문제
프론트 팀 깃허브에서 master에 merge를 하게되면 git actions 을 통해서 자동으로 S3에 그 내용이 갱신되도록 해놓았습니다. 그런데 S3에 내용이 갱신되었더라도 누군가는 반영이 안된 웹사이트를 보고 있거나 새로고침을 하면 오히려 이전의 내용으로 돌아가는 등의 문제가 있었습니다. 프론트 배포를 할 때 S3를 CloudFront와 연결하여 배포하였기 때문에 merge를 할 때마다 CloudFront 무효화 메뉴에서 /* 경로의 파일을 모두 무효화하도록 했습니다.

<br>

# 🛠사용자 피드백

### 1. xss 공격 대비
사용자 피드백을 위해 처음 서버를 열었을 때는 보안을 크게 의식하고 있지 않았습니다. 그런데 메인 게시판에 XSS 공격이 들어왔고, 게시글을 클릭하면 alert을 띄우거나 마이룸으로 이동하는 링크를 다른 사이트로 바꿔놓거나 아예 페이지에 접근할 수 없도록 하는 경우까지 있었습니다. 그래서 XSS 공격에 대응하는 방법으로 일단 백엔드에서 게시글을 작성 하는 등 사용자가 조회할 수 있는 텍스트들을 저장할 때 부등호 기호(<,>)를 전부 html 특수문자코드 (&lt;, &gt;)로 바꾸어 저장시키기로 했습니다. 게시글은 serializer을 통해 저장하도록 했기 때문에 validator를 커스텀해서 replace 함수로 문자열을 바꿔주는 식으로 코드를 수정했습니다.

```python
content_data = data.get('content')
if '<' in data.get('content'):
  content_data = content_data.replace('<', '&lt;')
  if '>' in data.get('content'):
    data['content'] = content_data.replace('>', '&gt;')
```

<br>

### 2. index.html로 돌아왔을 때 로그인을 다시해야하는 경우 방지
<br>[> 📑코드 보기 <](https://github.com/cmjcum/WM_front/blob/master/static/js/index.js#L6)
<br>로그인 후에 토큰 유효시간이 남아있더라도 기본 주소로 들어갈 경우 index.html로 이동되어서 로그인을 다시 해야만 메인 페이지로 접근 가능한 경우가 있어 불편하다는 사용자 피드백이 있었습니다. 그래서 index.html 페이지에 접근할 경우 사용자자가 발급받은 토큰의 시간과 현재시간을 비교해서 토큰 유효시간이 남아있을 경우 메인 페이지로 바로 이동시키도록 수정하였습니다.

<br>

# 🖋회고
<br>이 프로젝트에서 내가 맡은 역할은 배포였는데, 처음부터 끝까지 나혼자만 배포를 맡게되어서 좀 부담스러운 느낌이 있었다. 저번 프로젝트에서 배포와 관련해서 애로사항이 많아서 아예 프로젝트 초반부터 배포를 따로 준비하기로 한 건데, 이번에 원격강의로 도커를 배우게 되면서 도커로 배포를 하기로 결정하면서 더 팀원 중에서 도커를 아는 사람이 아무도 없어서 더 부담스러워졌다. 그래도 프로젝트 기간동안 따로 구글링과 유투브로 공부를 하고, 튜터님이 진행하신 도커 배포 특강을 통해 배포를 성공할 수 있었다. 오롯이 혼자 맡아서 성공하게 되서 여태껏 했던 프로젝트 중에 성취감이 가장 컸던 것 같다.
<br> 이번 프로젝트는 내일배움캠프에서 하는 마지막 프로젝트로 일주일 간의 사용자 피드백 반영기간이 있어서 구글폼으로 사용자의 다양한 요구와 시각을 받아 볼 수 있어서 정말 좋았다. 사용자 피드백을 읽고 깨달은 바가 많았다. 팀 코우미에서는 다수의 대중에게 친화적인 서비스보다는 컨셉이 있는 커뮤니티를 즐기는 소수의 사용자에게 익숙한 서비스를 제공하다보니 일반 사용자에게는 불친절한 면이 많았던 것 같다. 사이트를 처음 이용하는 사람들을 위해 사이트 이용 설명과 마이룸 꾸미기 도움말을 추가하고, 사용자가 눌러야하는 버튼에는 설명을 추가로 달고, 은유적인 표현을 쓴 곳은 직관적인 단어를 추가하여 사용자 편의성을 높였다. 그리고 최대한 이용하는 사람이 불편하지 않도록 UI부분도 일부 수정하였고, alert 창은 최대한 모달로 바꾸어 사이트를 이용하는 동안 일일이 alert창을 닫아야 하는 일도 줄였다. 
<br>이전에는 프로젝트들에서는 기획한 기능을 구현하는데 초점을 맞췄었는데, 이번에 사용자 피드백을 받아보니 사이트 이용시에 보안적인 문제와 사용자 편의 문제가 얼마나 중요한지 알게 된 것 같다. 앞으로 다른 프로젝트를 하게 되면 좀 더 기획단계에서부터 사용자를 고려하게될 것 같다.

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
