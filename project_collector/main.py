# 데이터를 수집할 수 있는 웹사이트 개발!
#  1. 화면: 특정 정보 입력(streamlit)
#  2. 수집: 데이터 수집(requests, beautifulSoup)
#  3. 화면: 출력, 엑셀 다운로드(streamlit, pandas)
#  4. 저장: 데이터베이스 저장(pymysql + MariaDB)

# 데이터를 수집하는 이유?
#   → 데이터 분석 or 인공지능 학습
#   → CSV or JSON 수집
# CSV 예: 1, 최체리, 10, 여
# JSON 예:
# {
#    "번호": 1,
#    "이름": "최체리",
#    "나이": 10,
#    "성별": 여
# }

from fnc_service import collect_news
import streamlit as st
from datetime import datetime

# streamlit run project_collector/main.py
# Streamlit docs → https://docs.streamlit.io/
# Emoji → https://snskeyboard.com/emoji/


def main():
    st.set_page_config(
        page_title="뉴스 수집기",                        # 제목
        page_icon="project_collector/img/favicon.png"   # 파비콘
    )
    st.title("NEWS :green[COLLECTOR]")
    st.text("실시간 뉴스를 수집합니다.")
    flag = False
    if st.button("수집"):
        df_news, count = collect_news()
        st.write(f"뉴스 {count}건 수집 완료!")
        st.write(df_news)
        flag = True
        # df_news : DataFrame → CSV type
        news_csv = df_news.to_csv(index=False, encoding="utf8")
    if flag:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        st.download_button(
            label = "다운로드",
            data = news_csv,
            file_name=f"실시간뉴스_{now}.csv",
            mime="text/csv",
            key="download_csv"
        )
        
    

if __name__ == "__main__":
    main()