import requests
from bs4 import BeautifulSoup
from naver import naver

base = "https://news.naver.com/section/"
tag_code = ["100", "101", "102", "103", "104", "105"]

headers = {"User-Agent" : "Chrome"}


for tag in tag_code : 
    # test_url = base + tag_code[0]

    url = base + tag

    response = requests.get(url, headers = headers)

    soup = BeautifulSoup(response.text, "html.parser")

    news_url = soup.find_all ("a", class_="sa_text_title _NLOG_IMPRESSION")

    for link in news_url :
        href = link.get("href")
        
        if href :
            try : 
                naver(href)
            except :
                print(href)
                continue
            
    # print(tag, " Done")

# print("All Done")
