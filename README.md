### Introduction
2021년 5월부터 고등학교 동창들과 등산을 다니기 시작했습니다. 등산을 다닐수록 친구들끼리 '우리가 어디어디 갔었지?'라는 질문을 하는 경우가 많아졌고, 자연스럽게 등산 기록을 지도로 한 눈에 볼 수 있으면 좋겠다는 생각에 python django와 kakao map api를 이용하여 개발하였습니다.
<br/><br />
<img src="https://github.com/nerdroid-labs/hiking-team/blob/master/example.png" width="300"/>

### Model
<img src="https://github.com/nerdroid-labs/hiking-team/blob/master/model.png" height="300"/>

+ **record**: 등산기록 테이블(날짜, 위도, 경도, 산 이름, *참여자)
  + 참여자는 member 테이블과 ManyToMany의 관계를 가짐 
+ **member**: 등산회원 테이블(이름)  
+ **photo**: 사진정보 테이블(*등산 기록, 이미지 파일 경로)
  + 등산 기록은 record 테이블의 id를 외래키로 가짐

### Install & Run(for debug)
```shell
python -m pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

### Before you start
시작하기 전에, **hiking_team/settings.py, line:25-26**의 SECRET_KEY와 KAKAO_MAP_API_KEY를 설정해야 합니다.
KAKAO_MAP_API_KEY는 https://apis.map.kakao.com 에서 발급 받을 수 있습니다.

### Get admin account
현재는 관리자 계정을 통해서만 데이터를 추가할 수 있기 때문에 관리자 계정을 생성하여야 합니다.
```shell
python manage.py createsuperuser
Username (leave blank to use $system-user-name): $username
Email address: $email
Password: $password
Password (again): $password
Superuser created successfully.
```

### Add data
서버 실행 후, http://{server_addr}/admin에 접속하여 member, record, photo순으로 등산 관련 데이터를 추가합니다.