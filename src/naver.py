import requests
from bs4 import BeautifulSoup
import re

from packaging import make_json

def naver (media, field) :

    # url = "https://media.naver.com/press/" + media + "?sid=" + field

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        return response.status_code
    
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h2", id = "title_area").text
    raw_contents = soup.find("article", id = "dic_area")
    # url
    reporter = re.sub(r"\s*기자\s*", "", soup.find("em", class_ = "media_end_head_journalist_name").text)
    # media
    # date
    # tag
    

if (__name__ == "__main__") :
    
    # media = 000  - 언론사 : 001 ~ ... 
    # field = 100  - 분야 : 100 ~ ...
    
    naver(0, 0)
