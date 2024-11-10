import requests
from bs4 import BeautifulSoup

media = 000  # 언론사 : 001 ~ ... 
field = 100  # 분야 : 100 ~ ...

def naver (media = 000, field = 100) :
    
    url = "https://media.naver.com/press/" + str(media) + "?sid=" + str(field)

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code == 200) :
        soup = BeautifulSoup(responce.text, "html.parser")
        print(soup)
        
    else : print(response.status_code)
    
    # news_content = soup.find("article", id = "dic_area")
    # print(news_content)


if (__name__ == "__main__") :
    naver()
