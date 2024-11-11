import requests
from bs4 import BeautifulSoup


def naver (num) :

    url = "https://media.naver.com/press/" + media_field[num][0] + "?sid=" + media_field[num][1]
    
    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code == 200) :
        soup = BeautifulSoup(responce.text, "html.parser")
        print(soup)
        
    else : print(response.status_code)
    
    # news_content = soup.find("article", id = "dic_area")
    # print(news_content)


if (__name__ == "__main__") :
    
    # media = 000  - 언론사 : 001 ~ ... 
    # field = 100  - 분야 : 100 ~ ...
    
    media_field = [["000", "100"], ["000", "101"]]
    naver(0)
