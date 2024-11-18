import requests
from bs4 import BeautifulSoup
import re

from packaging import make_json

def naver (media, field) :

    url = "https://media.naver.com/press/" + media + "?sid=" + field

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        return response.status_code
    
    soup = BeautifulSoup(response.text, "html.parser")


    # title
    title = soup.find("h2", id = "title_area").text

    # raw_contents
    raw_contents_with_tag = soup.find("article", id = "dic_area")
    raw_contents = str(raw_contents_with_tag)
    
    # url

    # reporter
    reporters = soup.find_all("em", class_="media_end_head_journalist_name")
    reporter = [re.sub(r"\s*기자\s*", "", reporter.text) for reporter in reporters]
    
    # media
    media = soup.find("span", class_ = "media_end_head_top_logo_text light_type _LAZY_LOADING_ERROR_SHOW").text
    
    # date :: f"YEAR.MONTH.DAY AM/PM TT:MM"
    date = soup.find("span", class_ = "media_end_head_info_datestamp_time _ARTICLE_DATE_TIME").text
    
    # tag
    active_tag = soup.find("li", class_ = "Nlist_item _LNB_ITEM is_active")
    tag = active_tag.find("span", class_="Nitem_link_menu").text


    make_json(title, raw_contents, url, reporter, media, date, tag)
    

if (__name__ == "__main__") :
    
    # media = 000  - 언론사 : 001 ~ ... 
    # field = 100  - 분야 : 100 ~ ...
    
    naver(0, 0)
