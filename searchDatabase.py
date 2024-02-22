from connect import *


def search_movies():
  try:
    field = input("Search by FilmID, Title, YearReleased, Rating, Duration, Genre: ")
 
    if field == "filmID":
                
      idInput = int(input("Enter filmID: "))
      dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (idInput,))
      row = dbCursor.fetchone()
 
      if row is None:
        print(f"No record with filmID {idInput} exists")
      else:
        for aMovie in row:
          print(aMovie)
 
    elif field in ["title", "yearReleased", "rating", "duration", "genre"]:
      strInput= input(f"Enter the value for the field {field}: ")
      dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{strInput}%'")
 
      rows = dbCursor.fetchall()
      if not rows:
        print(f"No record with field {field} matching '{strInput} ")
      else:
        for records in rows:
          print(records)
 
    else:
      print(f"Search field {field} invalid !")
      
  except sql.OperationalError as e:
    print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
    print(f"Not working because: {pe}")
  finally:
    print("DB operation performed")
    
if __name__ == "__main__":
  search_movies()