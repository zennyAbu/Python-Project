from connect import *

dbCursor.execute(""" 
CREATE TABLE "tbfilms" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"yearReleased"	INTEGER,
	"rating"	TEXT,
 "duration"	INTEGER,
 "genre"	TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)""")