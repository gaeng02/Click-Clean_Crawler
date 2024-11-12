import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/article/" + ""
    
headers = {"User-Agent" : "Chrome"}
    
response = requests.get(url, headers = headers)

if (response.status_code == 200) :
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find("h2", id = "title_area").get_text(strip = True)
    content = soup.find("article", id = "dic_area").get_text(strip = True)
    raw_content = soup.find("article", {"class" : "go_trans _article_content"})

    with open ("test.txt", "w") as f :
        f.write(title + "\n\n")
        f.write(content + "\n\n")
        f.write(str(raw_content))
        
else : print(response.status_code)
