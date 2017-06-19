import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-ORC/tesseract'

data=requests.get("http://sep.ucas.ac.cn/changePic")
with open ("1.jpg","wb") as f:
    f.write(data.content)
# print(data.content)
# imgfile=BytesIO(data.content)
# print(imgfile)
img1=Image.open("1.jpg")
gray=img1.convert('L')
gray.save("2.jpg")
bw=gray.point(lambda x: 0 if x<1 else 255 ,"1")
bw.save("3.jpg")
# print(img1)
# pytesseract.image_to_string(img1)
# print(pytesseract.image_to_string(img1))
res=pytesseract.image_to_string(bw)
print(res)
# print(data.content)