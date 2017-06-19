'''
from datetime import datetime 
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()
'''
'''
def webapplication(a, b):
    b('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (a['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

from wsgiref.simple_server import make_server
httpd=make_server("127.0.0.1",12345,webapplication)
print("start server on 12345")
httpd.serve_forever()
httpd.server_close()
'''
# a=input("enter you name")
# print("hello:{}".format(a))
# a=1
# print(f"hello:{a}")
# name=1
# print("hello！:{name}")
# d=dict()
# d["a"]=1
# d["b"]=2
# d["c"]=3
# print(d)
# d.pop("c")
# print(d)
# if("b" in d):
#     print("ok!")
# else:
#     print("no!")
# if(d.get("a",False)):
#     print(d["a"])
# else:
#     print("False")
# a=set()
# a.add(1)
# a.add(2)
# a.add(3)
# print(a)
# a.add((4,5,6,[7,8,9]))
# print(a)
# a.add(1)
# a.remove(3)
# print(a)
import math
def quadratic(a, b, c):
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

answer=quadratic(2,3,1)
print(answer)