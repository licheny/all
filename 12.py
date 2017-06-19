from bs4 import BeautifulSoup

data=[]
path="./web1.2/index.html"

try:
    with open(path,"r")as f:
        soup=BeautifulSoup(f.read(),"lxml")
        imgs=soup.select("body > div > div > div.col-md-9 > div > div > div > img")
        titles=soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")
        prices=soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
        # stars=soup.find_all("class=glyphicon glyphicon-star")
        stars=soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")
        # stars=soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p")
        reviews=soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
except IOError as fe:
    print("open file error")
# print(imgs)
# print(titles)
# print(stars)
for img,title,price,star,review in zip(imgs,titles,prices,stars,reviews):
    info={
         "img":img.get("src"),
         "title":title.get_text(),
         "price":price.get_text(),
         "star":len(star.find_all(class_="glyphicon glyphicon-star")),
         "review":review.get_text()
    }
    data.append(info)
# # print(data)

with open("result.txt","w") as f:
     for temp in data:
         print(temp["img"]+"\n"+temp["title"]+"\n"+temp["price"]+"\n"+str(temp["star"])+"\n"+temp["review"],file=f)
 
    

# <span class="glyphicon glyphicon-star"></span>