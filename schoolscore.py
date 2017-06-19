import urllib.request
import random
import http.cookiejar
import urllib.parse
import requests

url = 'http://sep.ucas.ac.cn/slogin'
header={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
params = {
          "userName": "lichenyang16@mails.ucas.ac.cn",
          "pwd": "140421199410151617",
          "sb": "sb"
}
# s=requests.Session()
r=requests.post(url,headers=header,params=params)
# print(r.cookies)
print(r.text)
# print(r)
# r=requests.get("http://jwxk.ucas.ac.cn/score/yjs/all")
# print(r.request.headers)
# print(r.headers)
# t=r.request.headers
# temp=t["cookie"].split("sepuser=")
# # print(temp[0])
# t1=temp[1]
# # print(isinstance(temp[0],str))
# t2=temp[0].split("=")[1].replace(";","")
# print(t1)
# print(t2)
# # print(t["cookie"].split("sepuser=")[0])
# # t2=t["cookie"].split()
# # print(t1)
# # print(t1)
# # r=requests.get("http://sep.ucas.ac.cn/appStore")
# # cookies=requests.utils.dict_from_cookiejar(r.cookies) 
# # print(cookies)
# # return cookies 
# cookies={
#     "JSESSIONID":t2,
#     "sepuser":t1
# }
# r=requests.get("http://jwxk.ucas.ac.cn",cookies=cookies,headers=header)
# print(r.headers)
# temp=r.headers
# # print(r.request.headers)
# t3=temp["Set-Cookie"].split("=")[1].split(";")[0]
# print(t3)
# cookies={
#     "JSESSIONID":t3,
#     "sepuser":t1
# }
# r=requests.get("http://jwxk.ucas.ac.cn/score/yjs/all",cookies=cookies,headers=header)
# print(r.session)
# print(r.headers)
# print(r.request.headers)
# print(r.text)
# JSESSIONID=EDEC810A5CAA00036DF1366FC63D6F96; sepuser="bWlkPTA4ZDYxNGQ0LTM2OTItNDc4MC05MWVlLWM1OTY0ZTZhOTkwNA==  "
# print(r.cookies.get("JSESSIONID"))
# print(r.cookies.get("sepuser"))
# JSESSIONID=EDEC810A5CAA00036DF1366FC63D6F96; sepuser="bWlkPTA4ZDYxNGQ0LTM2OTItNDc4MC05MWVlLWM1OTY0ZTZhOTkwNA==  "
# r=s.get("http://sep.ucas.ac.cn/appStore")
# r=s.post("http://jwxk.ucas.ac.cn/score/yjs/all")
# print(r.text)
# JSESSIONID=EDEC810A5CAA00036DF1366FC63D6F96; sepuser="bWlkPTA4ZDYxNGQ0LTM2OTItNDc4MC05MWVlLWM1OTY0ZTZhOTkwNA==  "
# print(r.cookies["sepuser"])
# print(r.content)
# t=s.get("http://jwxk.ucas.ac.cn/score/yjs/all")
# print(t.text)
# print (r.text) 
# url = 'http://sep.ucas.ac.cn/'
 
# params = {
#           "userName": "lichenyang16@mails.ucas.ac.cn",
#           "pwd": "140421199410151617",
#           "sb": "sb"
# }
 
# cookie = http.cookiejar.CookieJar()
# openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# openner.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
 
# data = urllib.parse.urlencode(params).encode()
# r= openner.open(url,data) 
# r=openner.open("http://jwxk.ucas.ac.cn/score/yjs/all") 

# print(r.read().decode())
# # f = open('alyy.html','w',encoding='utf-8')
# # f.write( r.read().decode())
# # f.close()