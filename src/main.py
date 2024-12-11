import time
import requests
from bs4 import BeautifulSoup
from naver import naver

def lambda_handler (event, context) :

    headers = {"User-Agent" : "Chrome"}


    # naver news
    base = "https://media.naver.com/press/"
    sid = "?sid="

    media_code = ["052", "055", "056",  "214", "437"]  
    tag_code = ["100", "101", "102", "103", "104"]

    except_media_code = ["052", "056"]
    except_tag = ["105"]
    
    for media in media_code :
        for tag in tag_code : 

            url = base + media + sid + tag

            response = requests.get(url, headers = headers)
            soup = BeautifulSoup(response.text, "html.parser")

            news_url = soup.find_all ("a", class_="press_edit_news_link _es_pc_link")

            for link in news_url :
                href = link.get("href")
                if href :
                    try :
                        time.sleep(1)
                        naver(href)
                        
                    except Exception as e :
                        print(f"{e} :: {href}")
                        continue

    # bbc news
    

if (__name__ == "__main__") :
    lambda_handler (True, True)   
