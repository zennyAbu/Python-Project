from connect import *
 
def delete_movie():
    try:
      filmID  = int(input("Enter the filmID to delete a movie : "))
      dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")
 
      row = dbCursor.fetchone()
 
      if row == None:
        print(f"FilmID {filmID} does not exits")
      else:
        dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (filmID,))
        dbCon.commit()
        print(f"The record {filmID} deleted from the Films table")
        
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")

if __name__ == "__main__":
  delete_movie()