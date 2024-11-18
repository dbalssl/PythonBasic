import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news


def collect_news(category:str):
    page = 1
    count = 1 # 뉴스기사 수
    while True:
        url = f"https://news.daum.net/breakingnews/{category}?page={page}"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        link_list = doc.select("ul.list_news2 a.link_txt")
        if len(link_list) == 0:
            break
        for link in link_list:
            print(f"{count} ==============================================")
            get_news_info(link["href"])
            count+=1
        page += 1
        

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