from connect import *
 
def insert_movies():
    try:
      mTitle = input("Enter movie Title: ")
      mYearReleased = input("Enter year movie was/is released: ")
      mRating = input("Enter movie rating: ")
      mDuration = input("Enter movie duration: ")
      mGenre = input("Enter movie genre: ")
 
      dbCursor.execute("INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES(NULL,?,?,?,?,?)", (mTitle, mYearReleased, mRating, mDuration, mGenre))
      dbCon.commit()
      print(f"{mTitle} inserted in the movies table")
      
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    except sql.Error as er:
        print(f"This error occurs: {er}")


if __name__ == "__main__":  
    insert_movies()