#Lee Yates
#CS-340
#11/28/2019
#7-1 Final Project
#Operations in Python
#Find a document with string input in MongoDB

import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_findDocument definition
def fp_findDocument(query,toDisplay):
  try:
    line = "--" * 45 
    print(line+"\n")
    result=collection.find(query,toDisplay)
    print(dumps(result))
    print(line+"\n")
    print("Processing Complete... \n")
  except ValidationError as ve:
    abort(400, str(ve))
  
#main program definition
def main():
  line = "--" * 45  
  print("\n\t\t   Find Documents Using The Industry Key Value \n")
  print(line+"\n")
  
  #prompt user for name of the industry
  industryname = raw_input("Enter The Name Of The Industry: ")
  query = {"Industry" : industryname}
  toDisplay = {"Ticker":1,"_id":0}
  print("Processing... \n")
  
  #call fp_findDocument
  fp_findDocument(query,toDisplay)
 
main()