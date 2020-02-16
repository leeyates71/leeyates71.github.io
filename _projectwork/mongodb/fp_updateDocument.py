#Lee Yates
#CS-340
#11/27/2019
#7-1 Final Project
#Operations in Python
#Update a document in MongoDB

import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_updateDocument definition
def fp_updateDocument(query,update):
  try:
    line = "--" * 50  
    collection.update_many(query,update)
    result=collection.find(query,{"Ticker":1,"Company":1,"Price":1,"Volume":1}).limit(10)
    print("RESULTS (First Ten Results)");
    print("--" * 50)
    print(dumps(result))
    print(line+"\n\n")
  except ValidationError as ve:
    abort(400, str(ve))
  
#main program definition
def main():
  line = "--" * 45  
  print(line+"\n\n")
  print("Provide The Ticker # for The Documents To Be Updated\n");
  print(line+"\n")
  
  #prompt user for ticker #
  tvalue = raw_input("Enter Ticker #: ")
  print("Received >>"+tvalue);
  print(">> The First Ten Results are Displayed Below");
  query = {"Ticker" : tvalue}
  result=collection.find(query,{"Ticker":1,"Company":1,"Price":1,"Volume":1}).limit(10)
  print(dumps(result))
  
  print(line+"\n") 
  print("Change Volume Value Of These Documents \n")
  
  #prompt user for new volume #
  volume = float(raw_input("New Volume #: "))
  print("Processing The Request..")
  print(line+"\n")
  update =  { "$set":{"Volume":volume}}
  
  #call fp_updateDocument
  fp_updateDocument(query,update)
  
main()