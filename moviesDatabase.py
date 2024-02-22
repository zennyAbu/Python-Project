from connect import *
from readDatabase import *

def add_data():
   with open("MOCK_DATA.sql") as md:
    
    sqlInsert = md.read()
    dbCursor.executescript(sqlInsert)
    
    movies_database()

if __name__ == "__main__":
  add_data()
