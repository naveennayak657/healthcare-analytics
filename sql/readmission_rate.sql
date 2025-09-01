SELECT 
    readmitted,
    COUNT(*) AS patient_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM diabetic_data), 2) AS percentage
FROM diabetic_data
GROUP BY readmitted;
