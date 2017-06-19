import requests
from bs4 import BeautifulSoup
import time
import pymongo

client=pymongo.MongoClient("localhost",27017)
infos=client["infos"]
urls=infos["urls"]
phone_number=infos["phone_number"]

def web_lists(url,page):
    url_lists=[]
    url_list= [url+"pn"+str(i)+"/" for i in range(1,page+1)]
    # print(url_list)
    for temp in url_list:
        time.sleep(1)
        data=requests.get(temp)
        soup=BeautifulSoup(data.text,"lxml")
        if soup.find_all("strong","number"):
            url_lists.append(temp)
            urls.insert_one({
                "url":temp
            })
            # print(temp)
        else:
            pass
    # print(url_lists)

def web_page(page):
    info_array=[]
    for temp in urls.find().limit(page):
        # print(temp["url"])
        data=requests.get(temp["url"])
        soup=BeautifulSoup(data.text,"lxml")
        # print(soup)
        titles=soup.select("strong.number")
        # print(titles)
        links=soup.select("a.t")
        # print(links)
        for title,link in zip(titles,links):
            # print(title,link)
            info={
                "title":title.get_text(),
                 "link":link.get("href")
            }
            info_array.append(info)
    phone_number.insert(info_array)
    # print(info_array)
    # print(len(info_array))
            
web_lists("http://bj.58.com/shoujihao/",5)
# web_page(1)
# web_page(116)
# print(phone_number.count())


