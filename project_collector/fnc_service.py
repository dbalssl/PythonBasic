import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd



options = Options()
#options.add_experimental_option("detach",True)
options.add_argument("headless") # 웹브라우저 (백그라운드)
options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])


def collect_news():
    count = 0 # 뉴스기사 수
    url = "https://news.daum.net/home"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    
    
    url_list = [] # 수집이 완료된 Link(URL)을 저장
    flag = False
    news_list = [] # 
    while True:
        # 9건의 기사 수집
        doc = BeautifulSoup(driver.page_source, "html.parser")
        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2")
        for link in link_list:
            # 중복수집 체크
            if link in url_list:
                flag = True
                break
            print(f"{count} ==============================================")
            news = get_news_info(link["href"])
            news_list.append(news)  # 수집한 데이터 로컬 저장
            count+=1
            url_list.append(link) # 중복수집 방지를 위한 처리
        if flag:
            break
        
        
        # [새로운 뉴스] 버튼 클릭 이벤트
        driver.find_element(By.XPATH, '//*[@id="58d84141-b8dd-413c-9500-447b39ec29b9"]/div[2]/a').click()
        time.sleep(1)
    
    # 수집한 데이터 27건 main으로 전달
    #  1. DB활용
    #   - DB(27건 저장) → SELECT 가져와서 전달
    #  2. 수집시 수집데이터를 따로 저장 후 전달
    #   - 
    # news_list → [{news1}, {news2}, {news3}, {news4}, ... , {news27}]
    # "pandas"의 DataFrame(표) Type으로 news_list 변환
    col_name = ["title", "writer", "content", "regdate"]
    df_news = pd.DataFrame(news_list, columns=col_name)  # DataFrame(표) 변환
    return df_news, count    

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
    insert_news(data)
    return data
    
