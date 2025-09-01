import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("../data/healthcare.db")

# choose which KPI to run (just change filename here)
sql_file = "../sql/top_admission_reasons.sql"

# read the query from file
query = open(sql_file, "r").read()

# run query
df = pd.read_sql_query(query, conn)

print(df)
