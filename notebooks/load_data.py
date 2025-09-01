import sqlite3
import pandas as pd

# Step 1: Read the CSV files
df_diabetic = pd.read_csv("../data/diabetes/diabetic_data_clean.csv")
df_ids = pd.read_csv("../data/diabetes/IDS_mapping.csv")

# Step 2: Connect to SQLite (creates healthcare.db inside /data)
conn = sqlite3.connect("../data/healthcare.db")

# Step 3: Write both CSVs into tables
df_diabetic.to_sql("diabetic_data", conn, if_exists="replace", index=False)
df_ids.to_sql("ids_mapping", conn, if_exists="replace", index=False)

print("✅ Both datasets loaded into healthcare.db successfully!")
