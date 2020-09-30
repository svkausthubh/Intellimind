import pymongo
from datetime import date

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Intellimind"]
mycol=mydb["NewsArticles"]
today=date.today()
def add(hash_mera):
    myquery={"title":hash_mera['title']}
    cursor=mycol.find(myquery).count()>0 

    if cursor == False:
        mycol.insert_one(hash_mera)
  
    
        