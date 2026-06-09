'''import sqlite3
conn = sqlite3.connect(r"database\processed\earthquakes_API.db") # Connexión a .db
cursor = conn.cursor()
cursor.execute("select count() from earthquakes_clean")
print(cursor.fetchall())
cursor.execute("Select name from sqlite_master where type='table'")
print(cursor.fetchall())'''
import sys
print(sys.executable)