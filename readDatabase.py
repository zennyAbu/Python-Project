from connect import *

def movies_database():
  try:
    dbCursor.execute("SELECT * FROM tblFilms")
    
    allMovies = dbCursor.fetchall()
    
    if allMovies:
      print("FilmID | Title | YearReleased | Rating | Duration | Genre")
      print("-" * 100)
      
      for aMovie in allMovies:
        print(f"{aMovie[0]:<2} | {aMovie[1]:<40} | {aMovie[2]:<5} | {aMovie[3]:<8} | {aMovie[4]:<5} | {aMovie[5]:<7}")
    else:
      print("No movies found in the movies table")
  
  except sql.OperationalError as e:
        print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
  
  finally:
    print("DB operation performed")

if __name__ == "__main__":
  movies_database()