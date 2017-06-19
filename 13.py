from bs4 import BeautifulSoup
import requests
import time

def web_page(url):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,"lxml")
    title=soup.select("h4 > em")
    address=soup.select("span.pr5") if soup.select("span.pr5") else ["null"]
    #div.con_l > div.pho_info > p > span
    price=soup.select("#pricePart > div.day_l > span")
    img=soup.select("#imgMouseCusor")
    pimg=soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > a > img")
    # sex=soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")
    sex="woman" if soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")[0].get("class")[0]=="member_ico1" else "man"
    name=soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")
    # print(address)
    # print(img)
    data={
        "title":title[0].get_text(),
        "address":address[0].get_text().strip() if address[0]!="null" else "null",
        "price":price[0].get_text(),
        "img":img[0].get("style"),
        "pimg":pimg[0].get("src"),
        "sex":sex,
        "name":name[0].get_text()
    }
    return data

def web_link():
    links_set=[]
    links=["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(30)]
    for link in links:
         web_data=requests.get(link)
         time.sleep(2)
         soup=BeautifulSoup(web_data.text,"lxml")
         src=soup.select("#page_list > ul > li > a")
         for temp in src:
             links_set.append(temp.get("href"))
    return links_set

# url="http://bj.xiaozhu.com/fangzi/5098280314.html"
# data=web_page(url)
# print(data)

web_links=web_link()
# print(web_links)
with open("13result.txt","w") as f:
    for link in web_links:
        print(link)
        data=web_page(link)
        # print(data["address"]
        print(data["title"]+"\n"+data["address"]+"\n"+str(data["price"])+"\n"+data["img"]+"\n"
        +data["pimg"]+"\n"+data["sex"]+"\n"+data["name"]+"\n",file=f)

    