import sqlite3

conn = sqlite3.connect('Users.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Users (Name TEXT, EMail TEXT, Mobile TEXT, City TEXT, State TEXT, Country TEXT, Password TEXT)')
print("Table created successfully")
conn.close()