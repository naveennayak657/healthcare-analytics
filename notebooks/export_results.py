import sqlite3
import pandas as pd
import os

# Paths
db_path = "../data/healthcare.db"
sql_dir = "../sql"
output_dir = "../data/kpi_results"

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

# KPI SQL files
kpi_files = [
    "top_admission_reasons.sql",
    "avg_length_of_stay.sql",
    "hospital_workload.sql",
    "avg_medications_by_race.sql",
    "readmission_rate.sql",
    "readmissions_by_age.sql"  
]

# Connect to database
conn = sqlite3.connect(db_path)

print("📥 Running KPI queries...")

for kpi in kpi_files:
    # Read SQL
    sql_file = os.path.join(sql_dir, kpi)
    query = open(sql_file, "r").read()

    # Run query
    df = pd.read_sql_query(query, conn)

    # Save result
    output_file = os.path.join(output_dir, kpi.replace(".sql", ".csv"))
    df.to_csv(output_file, index=False)

    print(f"✅ Saved: {output_file}")

conn.close()
print("\n🎉 All KPI results exported successfully!")
