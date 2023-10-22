import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설명
st.set_page_config( 
    page_icon='🌹',                          # 이모티콘 넣을 수 있는 곳
    page_title='지영이의 스트림릿 배포',      # 페이지 제목
    layout='wide' # 페이지를 넓은 화면으로 보기
)

st.subheader("도큐먼드")

if st.button("app.py 코드 보기"):
    code = """
    # 페이지 헤더, 서브헤더 제목 설정
    st.header("지영이의 페이지에 오신 걸 환영합니다 😊")
    st.subheader("✅ 스트림릿 기능 맛보기")

    # 페이지 컬럼 분할
    cols = st.columns((1,1,2))
    cols[0].metric("10/11", "15 'c", "2")
    cols[0].metric("10/12", "17 'c", "2 'F")
    cols[0].metric("10/13", "15 'c", "2")

    cols[1].metric("10/14", "17 'c", "2 'F")
    cols[1].metric("10/15", "14 'c", "-3 'F")
    cols[1].metric("10/16", "13 'c", "-1 'F")

    # 라인 그래프 데이터 생성 (with. pandas)
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c'])

    # 컬럼 나머지 부분에 라인 차트 생성
    cols[2].line_chart(chart_data)
    """
    st.code(code, language="python")