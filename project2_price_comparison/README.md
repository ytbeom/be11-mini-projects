# 🛍️ Streamlit 상품 가격 비교기

* Streamlit 기반 웹 애플리케이션으로, 사용자가 상품명을 입력하면 외부 API를 통해 해당 상품의 가격 비교 정보를 가져오고, 썸네일 이미지, 가격, 쇼핑몰 이름 등을 보여줍니다.
* 각 상품은 클릭 시 실제 쇼핑몰 페이지로 이동할 수 있습니다.

## 📁 프로젝트 구조
```
project2_price_comparison/
├── app.py # Streamlit 웹 인터페이스
├── api.py # 외부 API 호출 모듈
└── product.py # Product 클래스 정의
```

## 🚀 실행 방법

### 1. API 키 발급 및 .env 파일 추가

* 아래 내용을 참고해 네이버 검색 API CLIENT_ID와 CLIENT_SECRET을 발행합니다.
  * https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EC%82%AC%EC%A0%84-%EC%A4%80%EB%B9%84-%EC%82%AC%ED%95%AD
* `project2_price_comparison` 디렉토리 하위에 .env 파일을 만든 뒤 아래와 같은 식으로 적어둡니다.
```
CLIENT_ID=...
CLIENT_SECRET=...
```

### 2. Streamlit 실행

* `streamlit run app.py`를 실행하면 Streamlit 웹 어플리케이션이 실행됩니다.
* 실행 후 콘솔창에 나타나는 주소로 접속하면 Streamlit 웹 어플리케이션을 확인할 수 있습니다.

```bash
> python main.py

  ...
  Local URL: http://localhost:8501
  ...

```
