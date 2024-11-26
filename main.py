import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

def main():
  load_dotenv()
  
  input_database = input("What database would you like to use?\n").strip()
  output_dir = input("What is the output destination?\n").strip()
  
  client = MongoClient(os.getenv('URI'))
  db = client[input_database]
  collection_list = db.list_collection_names()
  
  for collection_name in collection_list:
    results = list(db[collection_name].find({}))
    results = json.loads(json.dumps(results, default=str))
    
    file_name = f"{input_database}.{collection_name}.json"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path,'w') as f:
      json.dump(results, f, indent=2)
  
  
  print('Backup Complete!')
  

if __name__ == "__main__":
  main()