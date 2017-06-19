import requests
from bs4 import BeautifulSoup
import time
import pymongo

data=requests.get("http://bj.58.com/shoujihao/pn2/")
soup=BeautifulSoup(data.text,"lxml")
if soup.find_all("strong","number"):
    print(soup)