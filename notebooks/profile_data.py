import pandas as pd

print("📥 Loading cleaned dataset...")
df = pd.read_csv("../data/diabetes/diabetic_data_clean.csv")

print(f"✅ Data shape: {df.shape}")

# 1. Missing values check
print("\n🔍 Missing values per column:")
print(df.isna().sum())

# 2. Unique values in key categorical columns
print("\n🧾 Unique categories:")
print("Gender:", df["gender"].unique())
print("Race:", df["race"].unique())
print("Weight (first 10):", df["weight"].unique()[:10])
print("Max Glucose Serum:", df["max_glu_serum"].unique())
print("A1Cresult:", df["A1Cresult"].unique())

# 3. Outlier check (numerical ranges)
print("\n📊 Numeric ranges:")
for col in ["time_in_hospital", "num_medications", "num_lab_procedures"]:
    print(f"{col}: Min={df[col].min()}, Max={df[col].max()}")

# 4. Diagnosis categories check
print("\n🩺 Diagnosis categories (diag_1):")
print(df["diag_1"].value_counts().head(10))

# 5. Duplicate rows
print("\n📑 Duplicate rows:", df.duplicated().sum())
