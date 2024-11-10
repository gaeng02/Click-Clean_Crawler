import requests
from bs4 import BeautifulSoup

field = ["sport", "business", "innovate", "culture", "arts", "travel", "earth"]  

def bbc (field = "sport") :
    
    url = "https://www.bbc.com/" + field

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code == 200) :
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)
        
    else : print(response.status_code)
    
    # news_content = soup.find("article", id = "dic_area")
    # print(news_content)


if (__name__ == "__main__") :
    bbc()
