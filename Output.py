import os
import json
import pymongo
from datetime import date

today=date.today()
curdate=date.today()

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Intellimind"]
mycol=mydb["NewsArticles"]
myquery={"Current_Date":"{}".format(str(today))}
list=mycol.find(myquery)

def outputdirectory():
    
    directory="{}".format(str(today))
    parent_directory="C:\kausthubh\Intellimind"
    path=os.path.join(parent_directory,directory)

    if not os.path.exists(path):
        os.mkdir(path)

    def writetojson(path,filename,data):
        filepath=path+'/'+filename+'.json'
        with open(filepath,'w') as fp:
            json.dump(data,fp,default=str)
    i=1
    for x in list:
        filename="{}".format(i)
        writetojson(path,filename,x)
        i+=1