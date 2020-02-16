#Lee Yates
#CS-340
#11/28/2019
#7-1 Final Project
#Operations in Python
#Find a document in MongoDB

import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_findDocument definition
def fp_findDocument(query):
  try:
    line = "--" * 45
    
    #count Number Of Documents Retrived
    result=collection.find(query).count()
    print(line +"\n")
    print("The Number Of Documents With 50-Day Simple Moving Average Between \n The Submitted Values "+str(result)+" Documents")
    print(line +"\n")
  
  except ValidationError as ve:
    abort(400, str(ve))
  
#main program definition
def main():
  line = "--" * 45  
  print("\t\t The Number Of Documents Having 50-Day Simple Moving Average \n\t\t Between The Values Provided ")
  print("\t\t Enter Two Numerical Values \n");
  print(line+"\n")
  
  #prompt user for greater than value
  high = float(raw_input("Enter Greater Than Value #: "))
  
  #prompt user for less than value
  low = float(raw_input ("Enter Less Than Value #: "))
  myDocument = { "50-Day Simple Moving Average" : {"$gt":high,"$lt":low}}
  
  #call fp_findDocument
  fp_findDocument(myDocument)

main()