import pandas as pd
import numpy as np

print("📥 Loading raw dataset...")
df = pd.read_csv("../data/diabetes/diabetic_data.csv")

print(f"✅ Raw data shape: {df.shape}")

# Step 1: Replace ? with NaN
df = df.replace("?", np.nan)

# Step 2: Fix invalid categories
df = df[df["gender"] != "Unknown/Invalid"]
df["race"] = df["race"].fillna("Unknown")
df["payer_code"] = df["payer_code"].fillna("Unknown")
df["medical_specialty"] = df["medical_specialty"].fillna("Unknown")

# Step 3: Clean up mixed-type columns
df["weight"] = df["weight"].replace(np.nan, "Unknown")

# Handle glucose & A1C results
df["max_glu_serum"] = df["max_glu_serum"].replace({"None": "Not Tested"})
df["A1Cresult"] = df["A1Cresult"].replace({"None": "Not Tested"})
df["max_glu_serum"] = df["max_glu_serum"].fillna("Not Tested")
df["A1Cresult"] = df["A1Cresult"].fillna("Not Tested")

# Step 4: Outlier handling (clip to realistic ranges)
df = df[df["time_in_hospital"] <= 14]
df = df[df["num_lab_procedures"] <= 132]
df = df[df["num_medications"] <= 80]

# Step 5: Group diagnosis codes
def map_diagnosis(code):
    try:
        code = float(code)
        if (390 <= code <= 459) or code == 785:
            return "Circulatory"
        elif (460 <= code <= 519) or code == 786:
            return "Respiratory"
        elif (520 <= code <= 579) or code == 787:
            return "Digestive"
        elif code == 250:
            return "Diabetes"
        elif 800 <= code <= 999:
            return "Injury"
        elif 710 <= code <= 739:
            return "Musculoskeletal"
        elif (580 <= code <= 629) or code == 788:
            return "Genitourinary"
        elif 140 <= code <= 239:
            return "Neoplasms"
        else:
            return "Other"
    except:
        return "Unknown"

for col in ["diag_1", "diag_2", "diag_3"]:
    df[col] = df[col].apply(map_diagnosis)

# Step 6: Remove duplicates
df = df.drop_duplicates()

# Step 7: Final missing value handling
# Replace any leftover NaN with "Not Tested"
df = df.fillna("Not Tested")

# Step 8: Save cleaned dataset
output_path = "../data/diabetes/diabetic_data_clean.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Cleaned dataset saved to: {output_path}")
print(f"✅ Cleaned data shape: {df.shape}")
