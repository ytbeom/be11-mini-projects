import streamlit as st

mentee_form_page = st.Page("mentee_form_page.py", title="멘티 등록 페이지")
mentor_matching_page = st.Page("mentor_matching_page.py", title="멘토 매칭 페이지")

pg = st.navigation([mentee_form_page, mentor_matching_page])
st.set_page_config(page_title="🤝 멘토-멘티 매칭 시스템", layout="wide")
pg.run()
