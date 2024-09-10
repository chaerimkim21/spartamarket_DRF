**spartamarket_DRF**

**📖 목차**

프로젝트 소개

주요기능

개발기간

기술스택

서비스 구조

API 명세서

ERD

프로젝트 파일 구조

Trouble Shooting


**👨‍🏫 프로젝트 소개**
스파르타코딩클럽의 팀 프로젝트로 개발된 중고거래 플랫폼 SPARTAMARKET을 DRF로 구현한 프로젝트입니다. 사용자는 회원 가입 후, 자신의 물건을 등록하고 업로드된 상품을 조회할 수 있습니다.

**💜 주요기능**
회원 가입 / 로그인 / 로그아웃 : 유저는 회원가입을 통해 플랫폼에 가입할 수 있으며, 로그인 후 서비스를 이용할 수 있습니다.

유저 프로필 조회 / 유저 정보 수정: 유저는 자신의 프로필 페이지에서 회원 정보를 확인할 수 있습니다.

판매할 물건 업로드 : 유저는 자신의 중고 물품을 등록하고 관리할 수 있습니다.


**⏲️ 개발기간**
2024.09.7(금) ~ 2024.09.10(수)


**📚️ 기술스택**
백엔드(Backend)
Python
Django
데이터베이스(Database)
SQLite

**기타 도구 및 라이브러리**

Git/GitHub

django-extensions

✔️ Language
Python: 백엔드 로직, 데이터 처리 및 API 개발을 위한 언어.
SQL: 데이터베이스 쿼리 및 관리에 사용.

✔️ Version Control
Git: 소스 코드 버전 관리 시스템. 프로젝트의 버전 기록을 유지하고 협업을 지원함.
GitHub: 원격 저장소 호스팅 서비스, 코드 리뷰 및 협업을 지원.

✔️ IDE
Visual Studio Code: Python, JavaScript, HTML/CSS의 개발을 위한 통합 개발 환경. 확장성 높은 플러그인 시스템 지원.

✔️ Framework
Django: Python 기반의 웹 프레임워크, Django REST Framework를 사용

✔️ DBMS
SQLite: 가벼운 관계형 데이터베이스 관리 시스템. 파일 기반의 데이터베이스로, 설정과 유지 관리가 간편하며, 로컬 개발과 작은 규모의 배포에 적합.


**서비스 구조**
- 백엔드: 데이터 처리, 비즈니스 로직 및 API를 처리.
- 데이터베이스: SQLite를 사용하여 사용자 및 상품 데이터를 저장 및 관리.
- API: 프론트엔드와 백엔드 간의 데이터 교환을 처리.


**API 명세서**
1. Accounts API
로그인 (Login)

![로그인 기능](https://github.com/user-attachments/assets/baf6f29c-5aee-457d-8ef9-44d631cf347d)

- Method: POST
- Endpoint: /api/accounts/login/
- Params: username, password

로그아웃 (Logout)

![로그아웃 기능](https://github.com/user-attachments/assets/fefc3cbc-625e-4c80-929d-51dc595fd937)

- Method: POST
- Endpoint: /api/accounts/logout/

회원가입 (Signup)

![회원가입 기능(포스트맨)](https://github.com/user-attachments/assets/ab4dcce6-2b5a-454b-9ab6-7c339704ab47)


- Method: POST
- Endpoint: /api/accounts/
- Params: username, password, email, first_name, last_name, nickname, birth(optional), introduction(optional)

프로필 조회

![프로필 조회](https://github.com/user-attachments/assets/b8644bbf-9cd4-4a50-aac8-613d69d7eceb)


- Method: GET
- Endpoint**: /api/accounts/<str:username>

프로필 수정 (Update Profile)

![회원 정보 수정](https://github.com/user-attachments/assets/32f35a5e-ca56-4e0c-a466-b3d4b6a8c1ac)


- Method: PUT
- Endpoint: /api/accounts/<str:username>/
- Params: username, email, nickname, birth(optional), introduction(optional)

회원 탈퇴 (Delete Account)

![회원 탈퇴 기능](https://github.com/user-attachments/assets/40e4e77d-35c2-4080-9ab6-c1b0bae1c403)


- Method: DELETE
- Endpoint: /api/accounts/
- Params: password


2. Products API
상품 목록 조회 (Products List)

![상품 조회 기능](https://github.com/user-attachments/assets/128a0387-a4de-4b3f-917c-df98dcd33a24)


- Method: GET
- Endpoint: /api/products/

상품 생성 (Create Product)

![상품 등록 기능](https://github.com/user-attachments/assets/e3c41ba4-f98c-4927-a6e5-2983581c8fdc)


- Method: POST
- Endpoint: /api/products/
- Params: title, content, image

상품 수정 (Update Product)

![상품 수정 기능](https://github.com/user-attachments/assets/6c5a896f-4d65-4ecb-ae21-0211c120d4f7)


- Method: PUT
- Endpoint: /api/products/<int:productId>/
- Params: title, content, image

상품 삭제 (Delete Product)

![상품 삭제 기능](https://github.com/user-attachments/assets/22c109d0-7514-4bc6-b475-300e41ddd209)


- Method: POST
- Endpoint: /api/products/<int:productId>/


**ERD**

![spartamarket_DRF ERD](https://github.com/user-attachments/assets/68fa5fdd-6d6f-4cee-b664-a178e268a664)


**프로젝트 파일 구조**
```
SpartaMarket/
├── accounts/               # 사용자 계정 관련 앱
│   └── *                   # 앱 관련 파일들 (admin.py, models.py, views.py 등)
├── media/                  # 미디어 파일 저장소
├── products/               # 제품 관련 앱
│   └── *                   # 앱 관련 파일들 (admin.py, models.py, views.py 등)
├── static/                 # 정적 파일들 (CSS, 이미지 등)
├── spartamarket/           # 프로젝트 설정 디렉터리
│   ├── settings.py         # 프로젝트 설정 파일
│   ├── urls.py             # 전역 URL 패턴 정의
├── manage.py               # Django 관리 커맨드 파일
└── README.md               # 프로젝트 설명서
```
**TroubleShooting**
https://velog.io/@crkim/TIL-%EB%82%B4%EC%9D%BC%EB%B0%B0%EC%9B%80%EC%BA%A0%ED%94%84-AI%EC%9B%B9%EA%B0%9C%EB%B0%9C7%EA%B8%B0-12%EC%A3%BC%EC%B0%A8-Day-53-2024.09.09
https://velog.io/@crkim/TIL-%EB%82%B4%EC%9D%BC%EB%B0%B0%EC%9B%80%EC%BA%A0%ED%94%84-AI%EC%9B%B9%EA%B0%9C%EB%B0%9C7%EA%B8%B0-12%EC%A3%BC%EC%B0%A8-Day-54-2024.09.10
