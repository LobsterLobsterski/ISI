import sqlite3

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.execute("select count(*) from penguins;")
rows = cursor.fetchall()
print(rows)