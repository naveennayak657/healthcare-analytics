SELECT 
    age,
    ROUND(100.0 * SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmit_lt_30_pct,
    ROUND(100.0 * SUM(CASE WHEN readmitted = '>30' THEN 1 ELSE 0 END) / COUNT(*), 2) AS readmit_gt_30_pct
FROM diabetic_data
GROUP BY age
ORDER BY age
