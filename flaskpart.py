import pymongo
from flask import Flask,jsonify,request
from datetime import date

app=Flask(__name__)

today=date.today()
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Intellimind"]
mycol=mydb["NewsArticles"]

@app.route('/')

def yahoo():
    myquery1={"Source":"Yahoo.com","Current_Date":str(today)}
    myquery2={"Source":"Reuters","Current_Date":str(today)}
    myquery3={"Source":"TimesOfIndia","Current_Date":str(today)}
    yahoo=mycol.find(myquery1).count()
    reuters=mycol.find(myquery2).count()
    times=mycol.find(myquery3).count()
    result={
        "Number Of Articles From Yahoo":yahoo,
        "Number Of Articles From Reuters":reuters,
        "Number Of Articles From TimesOfIndia":times
    }
    return jsonify(result)

@app.route('/Articles/<string:n>')

def articlesondate(n):
    myquery1={"Source":"Yahoo.com","Current_Date":n}
    myquery2={"Source":"Reuters","Current_Date":n}
    myquery3={"Source":"TimesOfIndia","Current_Date":n}
    yahoo=mycol.find(myquery1).count()
    reuters=mycol.find(myquery2).count()
    times=mycol.find(myquery3).count()
    result={
        "Number Of Articles From Yahoo On {}".format(n):yahoo,
        "Number Of Articles From Reuters On {}".format(n):reuters,
        "Number Of Articles From TimesOfIndia On {}".format(n):times
    }
    return jsonify(result)

@app.route('/companies',methods=['GET','POST'])

def compnaystats():
    if request.method=="POST":
        req=request.json
        company=req['company']#Security Should Be Entered
        myquery1={"Source":"Yahoo.com","security":str(company)}
        myquery2={"Source":"Reuters","security":str(company)}
        myquery3={"Source":"TimesOfIndia","security":str(company)}
        yahoo=mycol.find(myquery1).count()
        reuters=mycol.find(myquery2).count()
        times=mycol.find(myquery3).count()
        result={
            "Number Of Articles From Yahoo On {}".format(str(company)):yahoo,
            "Number Of Articles From Reuters On {}".format(str(company)):reuters,
            "Number Of Articles From TimesOfIndia On {}".format(str(company)):times
        }
        return jsonify(result)
        
if __name__=="__main__":
    app.run(debug=True)

