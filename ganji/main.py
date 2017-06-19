import requests
from bs4 import BeautifulSoup
from web_get_links import web_get_links
from multiprocessing import Pool
from web_get_classify import web_get_classify
import get_soure_html
# from get_soure_html import get_soure_html

links1=[temp["url"] for temp in get_soure_html.links.find()]
links2=[temp["url"] for temp in get_soure_html.content.find()]
links1=set(links1)
# print(len(links1))
links2=set(links2)
# print(len(links2))
url_links=links1-links2
# print(1)
# print(len(url_links))
channel=['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/', 'http://bj.ganji.com/shouji/', 'http://bj.ganji.com/shoujihaoma/', 'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/', 'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/', 'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/', 'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/', 'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/', 'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/', 'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/', 'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/']
def get_main_links(url):
    print(url)
    for i in range(1,101):
        # web_get_links(url,i)
        print(i)
        web_get_links(url,i)
        # if web_get_links(url,i):
        #     pass
        # else:
        #     break

if __name__ == "__main__":
    # data=web_get_classify()
    # print(data)
    pool1=Pool()
    # pool1.map(get_main_links,channel)
    pool1.map(get_soure_html.get_soure_html,url_links)
    pool1.close()
    pool1.join()
    # print(links1)
    # print(len(links1))
    # print(url_links)
    # print(links2)
    # pool=Pool()
    # print("1")
    # pool.map(get_soure_html.get_soure_html,url_links)
    # print("2")
    # pool.close()
    # pool.join()
    # for i in url_links:
    #     get_soure_html.get_soure_html(i)
    pass

