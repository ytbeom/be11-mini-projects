import pandas as pd
import streamlit as st

from db import get_mentee_list, get_mentor_list
from schemas import Mentee, Mentor


def match_mentor(mentee: Mentee, mentor_list: list[Mentor]) -> list[Mentor]:
    return mentor_list[0:3]


if "mentee_list" not in st.session_state:
    st.session_state.mentee_list = get_mentee_list()

if "mentor_list" not in st.session_state:
    st.session_state.mentor_list = get_mentor_list()

col1, col2 = st.columns(2)

with col1:
    st.header("👤 멘티 선택")
    
    selected_mentee = st.selectbox(
        "멘티를 선택하세요",
        st.session_state.mentee_list,
        format_func=lambda m: f"{m.name} ({m.desired_position})")

    st.subheader("📄 선택된 멘티 정보")
    st.write(selected_mentee.to_dict())

with col2:
    st.header("🧑‍🏫 멘토 목록")

    df = pd.DataFrame([
        {
            "이름": mentor.name,
            "회사": mentor.company,
            "직무": mentor.position,
            "지역": mentor.location,
            "기술스택": ", ".join(mentor.skills),
            "가능 요일": ", ".join(mentor.available_days),
            "MBTI": mentor.mbti
        }
        for mentor in st.session_state.mentor_list
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()
if st.button("🔍 멘토 추천"):
    # TODO: 파일 가장 위에 선언된 match_mentor 함수 완성시키기, 결과값은 Mentor 인스턴스의 list 형태여야 함
    matched = match_mentor(selected_mentee, st.session_state.mentor_list)
    # TODO

    st.subheader("✅ 추천된 멘토")
    if not matched:
        st.warning("조건에 맞는 멘토가 없습니다.")
    else:
        for m in matched:
            st.markdown(f"**{m.name}** ({m.position}, {m.company})")
            st.write(f"- 지역: {m.location}")
            st.write(f"- 기술스택: {', '.join(m.skills)}")
            st.write(f"- 가능 요일: {', '.join(m.available_days)}")
            st.write(f"- MBTI: {m.mbti}")
            st.divider()