import streamlit as st

from db import save_mentee


st.title("👩‍🎓 멘티 등록 페이지")

with st.form("mentee_form"):
    name = st.text_input("이름")
    location = st.selectbox("거주 지역", ["서울", "부산", "대구", "인천", "광주", "대전", "수원", "원격"])
    desired_position = st.selectbox("희망하는 업무", ["백엔드 개발자", "프론트엔드 개발자", "데이터 엔지니어", "DevOps", "AI 연구원"])
    level = st.radio("현재 수준", ["초급", "중급", "고급"])
    available_days = st.multiselect("가능한 요일", ["월", "화", "수", "목", "금", "토", "일"])
    mbti = st.selectbox("MBTI", [
        "ISTJ", "ISFJ", "INFJ", "INTJ",
        "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP",
        "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ])
    
    submitted = st.form_submit_button("저장하기")

if submitted:
    if not name:
        st.warning("이름을 입력해주세요.")
    elif not available_days:
        st.warning("가능한 요일을 최소 1개 선택해주세요.")
    else:
        mentee_data = {
            "name": name,
            "location": location,
            "desired_position": desired_position,
            "level": level,
            "available_days": available_days,
            "mbti": mbti
        }
        try:
            save_mentee(mentee_data)
            st.success("멘티 정보가 성공적으로 저장되었습니다!")
        except Exception as e:
            st.error(f"데이터 저장 중 오류 발생: {e}")
