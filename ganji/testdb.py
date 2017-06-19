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

content.insert_one({"test":"test"})