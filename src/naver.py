import requests
from bs4 import BeautifulSoup
import re

from packaging import make_json

def naver (_url) :

    url = _url

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        return response.status_code
    
    soup = BeautifulSoup(response.text, "html.parser")


    ''' title '''
    title = soup.find("h2", id = "title_area").text

    ''' body '''
    raw_contents_with_tag = soup.find("article", id = "dic_area")

    # data-src -> src
    for img in soup.find_all("img") :
        if 'data-src' in img.attrs :  
            img['src'] = img['data-src']  
            del img['data-src']

    # delete style = \"display: none;\
    for tag in soup.find_all(style = True) :  
        if 'display: none;' in tag['style'] :
            tag['style'] = tag['style'].replace('display: none;', '').strip()
            if not tag['style'] : del tag['style']

    body = str(raw_contents_with_tag)
    
    
    ''' url '''
    

    ''' author '''
    reporters = soup.find_all("em", class_="media_end_head_journalist_name")
    reporter = [re.sub(r"\s*기자\s*", "", reporter.text) for reporter in reporters]
    author = ", ".join(reporter)
    
    if author == "" :
        author = soup.find("span", class_ = "byline_s").text
        
    
    
    ''' media '''
    media = soup.find("span", class_ = "media_end_head_top_logo_text light_type _LAZY_LOADING_ERROR_SHOW").text

    
    ''' created_at '''
    # f"YEAR.MONTH.DAY AM/PM TT:MM"
    created_at = soup.find("span", class_ = "media_end_head_info_datestamp_time _ARTICLE_DATE_TIME").text

    
    ''' category ''' 
    active_tag = soup.find("li", class_ = "Nlist_item _LNB_ITEM is_active")
    category = active_tag.find("span", class_="Nitem_link_menu").text

    ''' image '''
    image_tag = soup.find("img")
    image_url = image_tag["src"] if image_tag else "None"

    ''' url '''
    __url = url.split("article/")[1].replace("/", "_")


    make_json(title, body, url, author, media, created_at, category, image_url, __url)
