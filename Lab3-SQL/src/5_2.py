import sqlite3

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor = cursor.execute("select species, island from penguins limit 5;")
while row := cursor.fetchone():
    print(row)