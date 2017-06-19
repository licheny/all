import requests,urllib.request
from bs4 import BeautifulSoup

url="http://weheartit.com/inspirations/taylorswift?page="

def get_web(url):
    imgs_src=[]
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,"lxml")
    imgs=soup.select("img.entry-thumbnail")
    for img in imgs:
        temp=img.get("src").replace("superthumb","large")
        imgs_src.append(temp)
    return imgs_src

def imgs_download(start,end):
    for i in range(start,end+1):
        imgs_links=get_web(url+str(i))
        count=1
        for temp in imgs_links:
            urllib.request.urlretrieve(temp,"./14imgs/"+str(count)+".jpg")
            count+=1



# data=get_web("http://weheartit.com/inspirations/taylorswift?page=18")
# print(data)
# tfp = open("N://pythonproject/14imgs/", 'wb')
# urllib.request.urlretrieve("http://shanxi.sinaimg.cn/cr/2012/1020/2283195682.jpg","./14imgs/1.jpg")
# imgs_download(1,2)
# <img alt="Taylor Swift, cute, and icon图片" src="http://data.whicdn.com/images/280233868/large.jpg">
# <img id="curBigImage" src="http://image.xiaozhustatic1.com/00,800,533/8,0,95,11929,1800,1200,a7c42f62.jpg" alt="" width="619.8874296435272" height="413">
# header={
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
# }
img_content=requests.get("http://data.whicdn.com/images/279656354/large.jpg")
if img_content.status_code==200:
    open("2.jpg","wb").write(img_content.content)

# <img alt="Taylor Swift" class="entry-thumbnail" height="250" src="http://data.whicdn.com/images/279656354/superthumb.webp" width="300">
# <img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="http://shanxi.sinaimg.cn/cr/2012/1020/2283195682.jpg" width="335" height="335" style="top: 0px; left: 336px; cursor: pointer; width: 242px; height: 242px; display: block;" log-rightclick="p=5.102" title="点击查看源网页">
# <img alt="Taylor Swift and candid图片" src="http://data.whicdn.com/images/279656354/large.jpg">