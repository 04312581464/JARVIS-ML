import requests
from bs4 import BeautifulSoup

classes = ["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee",
           "IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table",
           "dDoNo","ikb48b gsrt","sXLaOe","LWkfke","Ab33Nc","qv3Wpe","SPZz6b"]
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

def __about__(query,PRINT=False):
    query=query.replace(" + "," plus ")
    query=query.replace(" - "," minus ")
    URL = "https://www.google.com/search?q=" + query
    headers = {'User-Agent': useragent}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in classes:
        try:
            result=soup.find(class_=i).get_text()
            if PRINT:
                print("by class ",i)
            return result
        except Exception:
            pass
    return "no idea about that"
print(__about__("weather",True))