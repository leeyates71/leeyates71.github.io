#Lee Yates
#CS-340
#11/28/2019
#7-1 Final Project
#Operations in Python
#Aggregation Pipeline in MongoDB

import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient

#make a connection to the MongoDB market, collection stocks
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

#fp_aggregation defintion
def fp_aggregation(pipe):
  try:
    line = "--" * 45  
    print(line+"\n")
    result=collection.aggregate(pipe)
    result = dumps(result)
    print(result)
    print(line+"\n")
  except ValidationError as ve:
    abort(400, str(ve))
  
#main program definition
def main():
  line = "--" * 45  
  print("\n\t\t Aggregation Pipeline ")
  print(line+"\n")
  
  #prompt user for sector name
  sectorname = raw_input("Enter The Sector Name: ")
  firstStage = { '$match': { "Sector": sectorname } }
  secondStage= { '$group': { '_id': "$Industry", 'Total Outstanding Shares:': {'$sum': "$Shares Outstanding" } } }
  pipe = [firstStage,secondStage]
  
  #call fp_aggregation
  fp_aggregation(pipe)
  print("Processing Complete..\n")
  
main()