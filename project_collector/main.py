# 데이터를 수집할 수 있는 웹사이트 개발!
#  1. 화면: 특정 정보 입력(streamlit)
#  2. 수집: 데이터 수집(requests, beautifulSoup)
#  3. 화면: 출력, 엑셀 다운로드(streamlit, pandas)
#  4. 저장: 데이터베이스 저장(pymysql + MariaDB)
from fnc_service import collect_news
import streamlit as st

# streamlit run project_collector/main.py
# Streamlit docs → https://docs.streamlit.io/
# Emoji → https://snskeyboard.com/emoji/


def main():
    st.set_page_config(
        page_title="뉴스 수집기",                        # 제목
        page_icon="project_collector/img/favicon.png"   # 파비콘
    )
    st.title("NEWS :red[COLLECTOR]")
    st.text("실시간 뉴스를 수집합니다.")
    
    with st.form(key="form"):
        # 유효성 체크 → 사용자가 입력한 값이 유효한 값인지 체크
        #                ㄴ 전처리(가공) → 유효한 값으로 변경
        # 1. 정규식을 활용한 유효성 체크
        # 2. 엑셀 파일로 생성 다운로드
        # 3. github 정리 + README.md(꾸미기)
        submitted = st.form_submit_button("수집")
    
    # 버튼 이벤트 → 수집버튼을 클릭했을 때
    if submitted:
        collect_news()
    
if __name__ == "__main__":
    main()