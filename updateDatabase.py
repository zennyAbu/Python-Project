from connect import * 

def update_movies():
  try:
   
    filmID = int(input("Enter the filmID to update a movie: "))
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")
    
    # fetchone fetches a unique(one) record
    row = dbCursor.fetchone()
    # None is a single object to check if a value is present
    if row == None:
      print(f"No record with the SongID {filmID} exists")
    else:
      fieldname = input("Enter the field (title, yearReleased, rating, duration, genre) to update: ").title()
      fieldValue = input(f"Enter the value for {fieldname}: ")
            
      dbCursor.execute(f"UPDATE tblFilms SET {fieldname} = ? WHERE filmID = ?", (fieldValue, filmID))
      dbCon.commit()
  
  except sql.OperationalError as e:
        print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
  
  finally:
    print("DB operation performed")

if __name__ == "__main__":
  update_movies()