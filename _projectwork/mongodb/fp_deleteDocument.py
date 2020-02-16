#Lee Yates
#CS-340
#11/27/2019
#7-1 Final Project
#Operations in Python
#Delete a document in MongoDB

import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_deleteDocument definition
def fp_deleteDocument(document,tvalue):
  try:
    line = "--" * 45  
    print(line)
    result = collection.remove(document)
    print("\n--Documents With Ticker # "+tvalue+" Have Been Deleted  \n")
    print(dumps(result))
  except ValidationError as ve:
    abort(400, str(ve))
  
#main program definition
def main():
  line = "--" * 45  
  print(line+"\n")
  print("DELETE DOCUMENT\n")
  print("Provide The Ticker # for The Documents To Be Deleted, All Documents Associated With\nThat Ticker # Will Be Deleted \n");
  print(line+"\n")
  
  #prompt user for ticker #
  tvalue = raw_input("Enter Ticker Value #: ") 
  myquery = {"Ticker" : tvalue}
  print("\n" + "--" * 10 +" Listed Items Below Will Be Deleted " + "--" *10 + " \n")
  result=collection.find(myquery).limit(10)
  print(dumps(result))
  
  #call fp_deleteDocument
  fp_deleteDocument(myquery,tvalue)
  
main()