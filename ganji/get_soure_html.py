import requests
from bs4 import BeautifulSoup
import time
import pymongo
from web_get_classify import web_get_classify
import random
from multiprocessing import Pool

client=pymongo.MongoClient("localhost",27017)
ganji=client["ganji"]
links=ganji["links"]
content=ganji["cotent"]


def get_soure_html(url):
    print(url)
    header1={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "Cookie":"citydomain=bj; ganji_uuid=6985630376317028523329; ganji_xuuid=21e7dcaa-e360-48e5-86ef-9f9e31b90a09.1489325726807; webimverran=22; als=0; statistics_clientid=me; lg=1; crawler_uuid=148933467574902228183216; GANJISESSID=d211e6cf5d4920d8252ef8ba4f93fca9; _gj_txz=MTQ4OTMzNTY2MDoL/3SdwS26mA9VsGur3MLQikEhSA==; __utmt=1; 58uuid=d12c6458-eb76-4a81-948a-4dde7c88e6c8; new_session=0; init_refer=http%253A%252F%252Fbj.ganji.com%252Fwu%252F; new_uv=2; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A77726632264%7D; ganji_login_act=1489335080680; __utma=32156897.1222194765.1489325726.1489331687.1489335062.3; __utmb=32156897.5.10.1489335062; __utmc=32156897; __utmz=32156897.1489335062.3.3.utmcsr=ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/sorry/confirm.php",
        "Connection":"keep-alive"
        
    }
    header2={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Cookie":"ganji_login_act=1489337131957; citydomain=bj; ganji_uuid=2340233204780614707965; ganji_xuuid=e4f0a79c-885e-4f4c-c002-f271cc11d885.1489337132098; __utmt=1; __utma=32156897.335226204.1489337132.1489337132.1489337132.1; __utmb=32156897.1.10.1489337132; __utmc=32156897; __utmz=32156897.1489337132.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webimverran=55; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A2732085151%7D; crawler_uuid=148933714136153297250469; GANJISESSID=c04172e7647f8e94400fbbe7cd06a3ab; _gj_txz=MTQ4OTMzNzc1MDqbgChLjRH7l0fsT2csyq65SAGpQQ==; verified=1",
        "Connection":"keep-alive"
        
    }
    header3={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "cookie":"ganji_login_act=1489396849881; citydomain=bj; ganji_uuid=5440264823375861293917; ganji_xuuid=8c8c8253-4c4c-4e3c-9cf0-e5b604ae62f4.1489396852423; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A62452655301%7D; webimverran=99; __utma=32156897.1051827399.1489396882.1489396882.1489396882.1; __utmb=32156897.1.10.1489396882; __utmc=32156897; __utmz=32156897.1489396882.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1",
        "Connection":"keep-alive"
    }
    header4={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie":"ganji_login_act=1489397104344; citydomain=bj; __utma=32156897.1504521797.1489397105.1489397105.1489397105.1; __utmb=32156897.1.10.1489397105; __utmc=32156897; __utmz=32156897.1489397105.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; ganji_uuid=7521503599848718058646; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A62705166703%7D; ganji_xuuid=047080c4-c632-49cf-d1f6-d5b4b39f51fd.1489397105175; webimverran=21",
        "Connection":"keep-alive"
    }
    num=random.randint(0,4)
    if num==0:
        web_data=requests.get(url,headers=header1)
    elif num==1:
        web_data=requests.get(url,headers=header2)
    elif num==3:
        web_data=requests.get(url,headers=header3)
    else:
        web_data=requests.get(url,headers=header4)
    # print("3")
    soup=BeautifulSoup(web_data.text,"lxml")
    # print("4")
    # print(soup)
    # print(soup)
    # print(soup.find_all("h1","title-name"))
    if soup.find_all("h1","title-name"):
        data={
            "title":soup.select("h1.title-name")[0].get_text(),
            "time":soup.select("i.pr-5")[0].get_text().strip(),
            "views":soup.select("#pageviews")[0].get("data-text-format"),
            "price":soup.select("i.f22")[0].get_text(),
            "place":[temp.get_text() for temp in soup.select("ul.det-infor > li > a['target'=='_blank']")],
            "url":url
        }
        # print("5")
        content.insert_one(data)
        # print("6")
        # print(data["title"])
        # print(data)
        # with open ("ganji.txt","w") as f:
        #     print(data,file=f)
    elif soup.find_all("h1","info_titile"):
        data={
            "title":soup.select("h1.info_titile")[0].get_text() if len(soup.select("h1.info_titile"))!=0 else None,
            "time":"0",
            "views":soup.select("span.look_time")[0].get_text() if len(soup.select("span.look_time"))!=0 else None,
            "price":soup.select("span.price_now > i")[0].get_text() if len(soup.select("span.price_now > i"))!=0 else None,
            "place":soup.select("div.palce_li span i")[0].get_text() if len(soup.select("div.palce_li span i"))!=0 else None,
            "url":url
        }
        content.insert_one(data)
    else:
        # pass
        print("x")




# if __name__=="__main__":
#     count=0
#     links1=[temp["url"] for temp in links.find()]
#     print(len(links1))
#     links2=[temp["url"] for temp in content.find()]
#     print(len(links2))
#     links3=set(links1)
#     print(len(links3))
#     links4=set(links2)
#     print(len(links4))
#     url_links=links3-links4
#     # print(url_links)
#     print(len(url_links))
    # for i in url_links:
    #     count+=1
    #     get_soure_html(i)
    #     print(count)
#     get_soure_html("http://bj.ganji.com/jiaju/29129968969012x.htm")
#     pool=Pool()
#     # for url in links.find():
#     # pool.map()
#     urls=[]
#     # print(links.find(1))
#     for url in links.find().limit(20000):
#         # print(url["url"])
#         urls.append(url["url"])
#     pool.map(get_soure_html,urls)

