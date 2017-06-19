import pymongo
import time

client=pymongo.MongoClient("localhost",27017)
ganji=client["ganji"]
links=ganji["links"]
content=ganji["cotent"]
# links.remove()
# content.remove()
while True:
    time.sleep(2)
    # print(links.find().count())
    print(content.find().count())