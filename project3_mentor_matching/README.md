# 🤝 멘토-멘티 매칭 시스템 (Streamlit + MongoDB)

* 사용자가 멘티 정보를 입력하면 MongoDB에 저장되고, 저장된 멘토 목록과 비교하여 조건에 따라 적절한 멘토를 추천해주는 웹 기반 매칭 시스템입니다.

## 📁 프로젝트 구조

```
project3_mentor_matching/
├── app.py # Streamlit UI entrypoint
├── db.py # MongoDB 연결 및 데이터 저장/조회
├── mentee_form_page.py # 멘티 등록 페이지
├── mentor_matching_page.py # 멘토 매칭 페이지
└── schemas.py # 멘티, 멘토 클래스
```

## 🚀 실행 방법

### 1. `.env` 파일 생성
* `project3_mentor_matching` 디렉토리 하위에 .env 파일을 만든 뒤 아래와 같은 식으로 적어둡니다.
```
OWNER_ID=...
```
* 하나의 컬렉션에 여러 수강생의 데이터가 들어 있을 때, `OWNER_ID` 값을 사용해 본인이 생성한 데이터만 가져오게끔 작성되어 있습니다.
* 따라서 프로젝트를 진행하는 동안 `.env`의 `OWNER_ID` 값을 바꾸면 이전에 생성한 데이터를 읽어올 수 없습니다.

### 2. Streamlit 실행

* `streamlit run app.py`를 실행하면 Streamlit 웹 어플리케이션이 실행됩니다.
* 실행 후 콘솔창에 나타나는 주소로 접속하면 Streamlit 웹 어플리케이션을 확인할 수 있습니다.

```bash
> python main.py

  ...
  Local URL: http://localhost:8501
  ...

```
