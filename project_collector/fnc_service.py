import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_experimental_option("detach",True)
# options.add_argument("headless")
options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])


def collect_news():
    count = 0 # 뉴스기사 수
    url = "https://news.daum.net/home"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    
    # 숙제: 중복 방지 체크
    #  1P(9개 기사) → Total 3P(27개 기사) → 1번 수집(27개 기사)
    #  로직
    #   1. 다음 기사 수집 URL과 url_lisit의 URL을 비교
    #     → 있음(중복), 수집 멈춤
    #     → 없음, 수집 계속
    #   2. 기사 1건 수집 완료 → 해당 기사 URL을 url_list에 저장
    while True:
        # 9건의 기사 수집
        doc = BeautifulSoup(driver.page_source, "html.parser")
        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2")
        for link in link_list:
            print(f"{count} ==============================================")
            get_news_info(link["href"])
            count+=1
        # [새로운 뉴스] 버튼 클릭 이벤트
        driver.find_element(By.XPATH, '//*[@id="58d84141-b8dd-413c-9500-447b39ec29b9"]/div[2]/a').click()
        time.sleep(1)
        

def get_news_info(url: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    for text in contents:
        content += text.get_text()  
        
    writer_list = doc.select("span.txt_info")
    
    if len(writer_list) < 2:
        writer = ""
    else:
        writer = writer_list[0].get_text()
        
    writer = doc.select("span.txt_info")[0].get_text()
    reg_date = doc.select("span.num_date")[0].get_text()
    list_date = reg_date.split(". ")

    reg_date = list_date[0] + list_date[1] + list_date[2]
    print(f"뉴스 제목: {title}")
    print(f"뉴스 기자: {writer}")
    print(f"뉴스 날짜: {reg_date}")
    print(f"뉴스 본문: {content}")
    
    data = {
        "title": title,
        "writer": writer,
        "content": content,
        "regdate": reg_date,
    }
    #insert_news(data)
    
    
collect_news()