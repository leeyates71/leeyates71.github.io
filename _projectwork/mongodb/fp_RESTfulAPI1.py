#CRUD Operations in Python
#RESTful API in MongoDB

#!/usr/bin/python
import json
from bson import json_util
from bson.json_util import dumps
import bottle
from bottle import route, run, request, abort

#make a connection to the MongoDB market, collection stocks
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#URL paths for restfull services

#updating the stock by using the method PUT when key value is specified

@route('/updateStock/<TickerValue>', method='PUT')
def updateStock(TickerValue):
  
  #retreive all the data passed in the URL
  jsondata = request.json
  
  #query used to search documents that need updating
  query = { "Ticker" : TickerValue}
 
  #loop to update the collection using the parameters from the URL
  for key in jsondata:
    update =  { "$set":{key:jsondata[key]}}
    
    #updating collection
    collection.update(query,update)
  updateDocs = collection.find({"Ticker":TickerValue})
  
  #print a line
  line = "--" * 45 +"\n"
  result = dumps(updateDocs) #
  return line+"\nStock Details Successfully Updated \n"+str(result)+"\nEnd Of Stock \n"+line
  
#add document to the stocks colection
#no ticker value added

@route('/addStock', method='POST')
def addStock():
  
  #get all passed data in a json object
  jsonData = request.json
  
  #insert the document passed to the collection
  newDocument = collection.insert(jsonData)
  retriveDoc = collection.find_one({"_id":newDocument})
  line = "--" * 45 +"\n"
  
  #return inserted document  
  return line+ "\nStock Added \n "+dumps(retriveDoc)+"\nEnd Of Stock \n "+line

#ticker value is added
@route('/addStock/<tickerValue>', method='POST')
def addStock(tickerValue):
  
  #get all passed data in a json object
  jsonData = request.json
  jsonData.update( {'Ticker' : tickerValue} )
  
  #insert the document passed to the collection
  recordId = collection.insert(jsonData)
  retriveDoc = collection.find_one({"_id":recordId})
  line = "--" * 45 +"\n"
  
  #return inserted document
  return line+ "\nStock Added \n "+dumps(retriveDoc)+" \nEnd Of Stock \n "+line

#deleting data

@route('/removeStock/<TickerValue>', method='GET')
def removeStock(TickerValue):
  
  #query to search target data
  query = {"Ticker" :TickerValue}
  
  #delete all documents that matching the query
  result = collection.delete_many(query)
  
  #return results to the user
  return "\nStock Has Been Deleted.... \n"

#reading data from collection given ticker value

@route('/getStock/<TickerValue>', method='GET')
def getStock(TickerValue):
  readDocument = collection.find({"Ticker":TickerValue})
  line = "--" * 45 +"\n"
  return line+"\nThis Is The Requested Stock \n "+dumps(readDocument)+" \nEnd Of Requested Stock \n"

#no parameter is added
@route('/getStock', method='GET')
def getStock():
  
  #first record will display
  readDocument = collection.find().limit(1)
  line = "--" * 45 +"\n"
  return line+"\nThis Is The Requested Stock \n "+dumps(readDocument)+" \nEnd Of Requested Stock \n"

#getting company stock report

#URLs replace spaces with + 
#replace the spaces with + sign
@route('/companyReport/<companyName>', method='GET')
def getReport(companyName):
  company = companyName.replace("+"," ")
  
  #pipeline is composed of multiple stages
   
  #stage one
  print("\n\n\n "+company+"\n\n")
  result2 = CompanyPipeline(company)
  firstStage = { '$project': {'Company':1,'Float Short':1,'Relative Volume':1,'Volume':1,'Performance (Year)':1 } }
  
  #stage two
  secondStage = { '$match': { "Company": company } }
  print("\n\n\n "+str(secondStage)+"\n\n")
  
  #stage three
  thirdStage = { '$group': { '_id': "$Company",'Total Float Short': {'$sum': "$Float Short" },
                           'Average Relative Volume':{'$avg':"$Relative Volume"},
                           'Average Volume':{'$avg':'$Volume'},
                           'Max Performance (Year)':{'$max':'$Performance (Year)'},
                           'Total Volume':{'$sum':'$Volume'} } }
  
  #adding limit
  fourthStage = { '$limit' : 5 }
  query = [firstStage,secondStage,thirdStage,fourthStage]
  print(str(query))
  result=collection.aggregate(query)
  results = dumps(result)
  
  #print results
  return "-------- \n \t\t\t Stock Report For ["+company+"] Company \n\n--------\nInformation\n\n"+results+" \n-------- \n"+result2+"\n"

#end of company report

#this pipeline will retreive data depending on specified data 

#CompanyPipeline definition used with getting a company stock report
def CompanyPipeline(company):
  
  #stage one specifies the fields to be passed to the next stages
  firstStage = { '$project': { 'Company':1,'Float Short':1,'Price':1,'Average True Range':1,'50-Day Simple Moving Average':1,'Change':1 } }
  
  #stage two
  secondStage = { '$match': { "Company": company } }
  
  #stage three performs all operations
  thirdStage = { '$group': { '_id': "$Company", 'Total Float Short': {'$sum': "$Float Short" },
                           'Average Average True Range':{'$avg':"$Average True Range"},
                           'Total Price':{'$sum':'$Price'},
                           'Max 50-Day Simple Moving Average (Year)':{'$max':'$50-Day Simple Moving Average'},
                           'Minimum Change':{'$min':'$Change'} } }
  
  #add limit
  fourthStage = { '$limit' : 5 }
  myQuery = [firstStage,secondStage,thirdStage,fourthStage]
  result=collection.aggregate(myQuery) 
  result = dumps(result)
  return "-------- \nAdditional Information \n\n"+result+"\n\n"

#getting country report

#URLs replace spaces with + 
#replace the spaces with + sign
@route('/countryReport/<countryName>', method='GET')
def getReport(countryName):
  country = countryName.replace("+"," ")
  
  #pipeline is composed of multiple stages
   
  #stage one
  print("\n\n\n "+country+"\n\n")
  result2 = CountryPipeline(country)
  firstStage = { '$project': {'Country':1, 'Ticker':1,'Float Short':1,'Relative Volume':1,'Volume':1,'Performance (Year)':1 } }
  
  #stage two
  secondStage = { '$match': { "Country": country } }
  print("\n\n\n "+str(secondStage)+"\n\n")
  
  #stage three
  thirdStage = { '$group': { '_id': "$Country", 'Total Float Short': {'$sum': "$Float Short" },
                           'Average Relative Volume':{'$avg':"$Relative Volume"},
                           'Average Volume':{'$avg':'$Volume'},
                           'Max Performance (Year)':{'$max':'$Performance (Year)'},
                           'Total Volume':{'$sum':'$Volume'} } }
  
  #adding limit
  fourthStage = { '$limit' : 5 }
  query = [firstStage,secondStage,thirdStage,fourthStage]
  print(str(query))
  result=collection.aggregate(query)
  results = dumps(result)
  
  #print results
  return "-------- \n \t\t\t Portfolio Report For ["+country+"] Country \n\n--------\nInformation\n\n"+results+" \n-------- \n"+result2+"\n"

#end of country report
#this pipeline will retreive data depending on specified data 

#CountryPipeline definition used with getting country report
def CountryPipeline(country):
  
  #stage one specifies the fields to be passed to the next stages
  firstStage = { '$project': { 'Country':1,'Float Short':1,'Price':1,'Average True Range':1,'50-Day Simple Moving Average':1,'Change':1 } }
  
  #stage two
  secondStage = { '$match': { "Country": country } }
  
  #stage three performs all operations
  thirdStage = { '$group': { '_id': "$Country", 'Total Float Short': {'$sum': "$Float Short" },
                           'Average Average True Range':{'$avg':"$Average True Range"},
                           'Total Price':{'$sum':'$Price'},
                           'Max 50-Day Simple Moving Average (Year)':{'$max':'$50-Day Simple Moving Average'},
                           'Minimum Change':{'$min':'$Change'} } }
  
  #add limit
  fourthStage = { '$limit' : 5 }
  myQuery = [firstStage,secondStage,thirdStage,fourthStage]
  result=collection.aggregate(myQuery) 
  result = dumps(result)
  return "-------- \nAdditional Information \n\n"+result+"\n\n"

#getting industry report

#URLs replace spaces with + 
#replace the spaces with + sign
@route('/industryReport/<industryName>', method='GET')
def getReport(industryName):
  industry = industryName.replace("+"," ")
  
  #pipeline is composed of multiple stages
   
  #stage one
  print("\n\n\n "+industry+"\n\n")
  result2 = IndustryPipeline(industry)
  firstStage = { '$project': {'Industry':1, 'Ticker':1,'Float Short':1,'Relative Volume':1,'Volume':1,'Performance (Year)':1 } }
  
  #stage two
  secondStage = { '$match': { "Industry": industry } }
  print("\n\n\n "+str(secondStage)+"\n\n")
  
  #stage three
  thirdStage = { '$group': { '_id': "$Industry", 'Total Float Short': {'$sum': "$Float Short" },
                           'Average Relative Volume':{'$avg':"$Relative Volume"},
                           'Average Volume':{'$avg':'$Volume'},
                           'Max Performance (Year)':{'$max':'$Performance (Year)'},
                           'Total Volume':{'$sum':'$Volume'} } }
  
  #adding limit
  fourthStage = { '$limit' : 5 }
  query = [firstStage,secondStage,thirdStage,fourthStage]
  print(str(query))
  result=collection.aggregate(query)
  results = dumps(result)
  
  #print results
  return "-------- \n \t\t\t Portfolio Report For ["+industry+"] Industrie(s) \n\n--------\nInformation\n\n"+results+" \n-------- \n"+result2+"\n"

#end of industry report
#this pipeline will retreive data depending on specified data 

#IndustryPipeline definition used with getting industry report
def IndustryPipeline(industry):
  
  #stage one specifies the fields to be passed to the next stages
  firstStage = { '$project': { 'Industry':1,'Float Short':1,'Price':1,'Average True Range':1,'50-Day Simple Moving Average':1,'Change':1 } }
  
  #stage two
  secondStage = { '$match': { "Industry": industry } }
  
  #stage three performs all operations
  thirdStage = { '$group': { '_id': "$Industry", 'Total Float Short': {'$sum': "$Float Short" },
                           'Average Average True Range':{'$avg':"$Average True Range"},
                           'Total Price':{'$sum':'$Price'},
                           'Max 50-Day Simple Moving Average (Year)':{'$max':'$50-Day Simple Moving Average'},
                           'Minimum Change':{'$min':'$Change'} } }
  
  #add limit
  fourthStage = { '$limit' : 5 }
  myQuery = [firstStage,secondStage,thirdStage,fourthStage]
  result=collection.aggregate(myQuery) 
  result = dumps(result)
  return "-------- \nAdditional Information \n\n"+result+"\n\n"

#main program
  
if __name__ == '__main__':
  run(debug=True,reloader = True)
  #run(host='localhost', port=8080)