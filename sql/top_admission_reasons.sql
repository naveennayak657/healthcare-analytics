SELECT 
    m.description AS admission_reason,
    COUNT(*) AS total_admissions
FROM diabetic_data d
JOIN ids_mapping m 
    ON d.admission_type_id = m.admission_type_id
GROUP BY m.description
ORDER BY total_admissions DESC
LIMIT 5
