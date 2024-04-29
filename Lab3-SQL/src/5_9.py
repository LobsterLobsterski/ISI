import pandas as pd
import sqlite3
import sys

db_path = 'C:/Users/tomas/Desktop/szkola/ISI/Lab3-SQL/db/penguins.db'
connection = sqlite3.connect(db_path)
query = "select species, count(*) as num from penguins group by species;"
df = pd.read_sql(query, connection)
print(df)