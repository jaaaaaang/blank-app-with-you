import streamlit as st

# 페이지 제목 설정
st.title("My Streamlit App")
st.header("Header of the page")
st.subheader("Subheader section")

# 사용자 입력 받기
name = st.text_input("What's your name?")
st.write(f"Hello, {name}!")

# 버튼 추가
if st.button('Click Me'):
    st.write("You clicked the button!")

# 그래프 또는 차트 출력
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터프레임 생성
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

st.line_chart(data)

