import streamlit as st

# Streamlit 앱 제목
st.title("Multiply Service API Test")

# POST 요청 데이터 시뮬레이션
if "multiplier" not in st.session_state:
    st.session_state.multiplier = None

# 사용자 요청 처리
with st.form(key="api_form"):
    number = st.number_input("Enter a number", value=0)
    submit = st.form_submit_button("Multiply!")

    if submit:
        # 입력값은 number  (100배를 증가해서 리턴)
        calculate_res = (number * 100)

st.text_input("run_this")
