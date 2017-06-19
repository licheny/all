import requests
from bs4 import BeautifulSoup
import time
# print("hello")
def web_get_classify():
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "cookie":"ganji_login_act=1489337131957; citydomain=bj; ganji_uuid=2340233204780614707965; ganji_xuuid=e4f0a79c-885e-4f4c-c002-f271cc11d885.1489337132098; __utmt=1; __utma=32156897.335226204.1489337132.1489337132.1489337132.1; __utmb=32156897.1.10.1489337132; __utmc=32156897; __utmz=32156897.1489337132.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webimverran=55; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A2732085151%7D; crawler_uuid=148933714136153297250469; GANJISESSID=c04172e7647f8e94400fbbe7cd06a3ab; _gj_txz=MTQ4OTMzNzc1MDqbgChLjRH7l0fsT2csyq65SAGpQQ==; verified=1"
        
    }
    data=[]
    web_data=requests.get("http://bj.ganji.com/wu/",headers=header)
    # print(web_data)
    soup=BeautifulSoup(web_data.text,"lxml")
    # print(soup)
    links=soup.select("dl.fenlei > dt > a")
    #wrapper > div.content > div:nth-child(1) > div:nth-child(1) > dl > dt > a:nth-child(1)
    # print(links)
    for link in links:
        data.append("http://bj.ganji.com"+link.get("href"))
    print(data)
    # print(len(data))
    return data

if __name__ == "__main__":
    web_get_classify()