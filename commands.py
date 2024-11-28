import os
from pprint import pprint
from pymongo import MongoClient
from dotenv import load_dotenv

def get_db_names(mongo_client):
  names = mongo_client.list_database_names()
  # name_columns = two_dimensional_list(names, 4)

  # pprint(name_columns)
  print_columns(names, 4)
  

# TODO
def print_columns(flat_list, num_columns):
  column_index = 0
  rowish_index = 0
  items = []
  
  while column_index < num_columns:
    items.append(flat_list[current_column])
    current_column += num_columns
    if current_column >= len(flat_list):
      starting_i += 1
      current_column = starting_i
      row = '\t\t'.join(items)
      print(row)
      items = []

# (0, a*0), (1, a*0 + 1), (2, a*0 + 2), (3, a*0 + 3), (4, a * 1), (5, a * 1 + 1), (6, a * 1 + 2), 
# (num_columns * column_index) + rowish_index  


if __name__ == "__main__":
  load_dotenv()
  client = MongoClient(os.getenv('URI'))

  get_db_names(client)