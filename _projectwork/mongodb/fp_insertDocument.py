#Lee Yates
#CS-340
#11/27/2019
#7-1 Final Project
#Operations in Python
#Insert a document in MongoDB

import json
from bson import json_util
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_insertDocument definition
def fp_insertDocument(document):
  message = ""
  try:
    result=collection.insert(document)
    message = "\nDocument Added Successfully"
  except ValidationError as ve:
    abort(400, str(ve))
    message = "Document Could Not Be Added"
  return message

#main program definition
def main():
  line = "--" * 45  
  print(line+"\n")
  
  #prompt user for document input
  document = raw_input("Enter Your Document: ")
  print("\nProcessing Document.....\n\n"+line+"\n")
  print(document)
  
  #call fp_insertDocument
  print fp_insertDocument(json.loads(document))
  print("\nInsert Document Process Complete\n")
  print(line+"\n\n")
  
main()