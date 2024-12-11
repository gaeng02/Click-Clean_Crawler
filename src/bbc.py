import requests
from bs4 import BeautifulSoup

def bbc () :
    
    url = "https://www.bbc.com/news"

    headers = {"User-Agent" : "Chrome"}
    
    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        print(response.status_code)
        return ;

    soup = BeautifulSoup(response.text, "html.parser")

    news_links = soup.find_all('a', {'data-test' : True, 'id' : 'internal-link'})
