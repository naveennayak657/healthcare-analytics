📊 Healthcare Analytics – Diabetes Readmission Insights
🚀 End-to-End Data Analytics Project | SQL • Python • Snowflake (SQLite) • Tableau/Power BI
👤 Author: [Naveen Vishlavath](https://www.linkedin.com/in/naveen-v-b6563a308/)

This project demonstrates how raw healthcare data can be transformed into business-ready insights. Using a real diabetes dataset, I built an end-to-end pipeline that covers data cleaning, database integration, SQL KPIs, and visualization readiness — replicating real-world healthcare analytics scenarios.

🏥 Business Problem
Hospital readmissions are one of the most critical metrics in healthcare. They directly impact:
• Patient outcomes (continuity of care, risk management)
• Hospital costs (penalties, resource strain)
• Policy compliance (CMS, insurance reimbursements)
This project focuses on analyzing diabetes patient admissions, uncovering drivers of readmission, and providing KPIs that hospital leadership could use to improve outcomes.

📂 Project Workflow
🔹 1. Data Source
Dataset: Diabetes 130-US hospitals dataset (Kaggle)
Records: 101,766 patient encounters
Columns: 50 features (demographics, diagnoses, medications, outcomes)

🔹 2. Data Cleaning (Python: Pandas, NumPy)
Replaced invalid/missing values (?, None) with standard categories (e.g., Unknown, Not Tested).
Mapped ICD-9 diagnosis codes into medical categories (Circulatory, Respiratory, Diabetes, Injury, etc.).
Removed duplicates and clipped outliers (e.g., stay > 14 days).
Created a clean dataset: diabetic_data_clean.csv.

🔹 3. Database Integration (SQLite)
Loaded clean dataset into SQLite database (healthcare.db).
Designed SQL queries for KPI generation.

🔹 4. KPI Development (SQL + Pandas)
Created queries to measure admission trends, workload, medications, and readmissions.
Exported results into kpi_results/ for visualization.

🔹 5. Dashboarding (Power BI / Tableau – coming soon)
Interactive dashboards will summarize KPIs for executive decision-making.

📌 Key KPIs & Insights
1) Top Admission Reasons
   • Identifies most common causes of admission (Emergency, Elective, Referrals).
2) Average Length of Stay
   • Patients stayed ~4.4 days on average.
3) Hospital Workload
   • Avg. 43 lab procedures and 1.3 other procedures per admission.
4) Medications by Race
   • Avg. meds prescribed ranged from 13 (Asian) → 16 (Caucasian).
5) Readmission Rate
   • <30 days: 11% • >30 days: 35% • No readmission: 54%.
6) Readmissions by Age Group
   • Highest risk: Patients aged 70–90, with ~36% readmission rate.

📊 Example KPI Output  

| KPI                      | Result (Sample)                         |  
|--------------------------|-----------------------------------------|  
| Avg. Length of Stay      | 4.4 days                                |  
| Readmission Rate         | <30 days: 11% • >30 days: 35% • No: 54% |  
| Top Admission Reasons    | Emergency, Elective, Physician Referral |  
| Avg. Medications by Race | Caucasian: 16 • Asian: 13 • Hispanic: 14|  

## 📊 Dashboards  
Interactive dashboards (Power BI / Tableau) are being developed and will be added soon.  
They will include visualizations for:  
- Top admission reasons  
- Readmission trends by age & time  
- Hospital workload & length of stay  
- Medications distribution by race  

Stay tuned — screenshots and a Tableau Public link will be added here soon!  

## 📂 Repository Structure  

📁 healthcare-analytics/  
├── data/                 # Raw, cleaned data & KPI results  
│   ├── diabetes/         # Original Kaggle dataset  
│   └── kpi_results/      # Exported KPI CSVs  
├── notebooks/            # Python scripts (cleaning, profiling, exporting)  
├── sql/                  # SQL queries for KPIs  
├── README.md             # Project documentation  
└── healthcare.db         # SQLite database  

🛠️ Tech Stack
– Programming: Python (Pandas, NumPy)
– Database: SQLite3 (easily transferable to Snowflake/Postgres)
– Visualization: Tableau / Power BI (Dashboards to follow)
– Version Control: Git & GitHub
– Domain: Clinical Healthcare Analytics

📈 Future Enhancements
– Build interactive dashboards in Tableau & Power BI.
– Add predictive modeling (ML) for readmission risk scores.
– Extend pipeline to Snowflake cloud data warehouse.
– Deploy with Streamlit for interactive exploration.

📑 How to Run
1) Clone the repo:
   ```bash
   git clone https://github.com/naveennayak657/healthcare-analytics.git
   cd healthcare-analytics
   ```
2) Install dependencies:
   ```bash
   pip install pandas numpy sqlite3
   ```
3) Clean & load data:
   ```bash
   python notebooks/deep_clean_data.py
   python notebooks/load_data.py
   ```
4) Run KPI queries:
   ```bash
   python notebooks/export_results.py
   ```
5) View results in:
   ```bash
   data/kpi_results/
   ```
## 🔑 Keywords  
Data Analytics, SQL, Python, Snowflake, SQLite, Tableau, Power BI, Healthcare Analytics, ETL, KPI Development, Data Cleaning, Machine Learning Ready  

   
