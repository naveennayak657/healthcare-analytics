SELECT 
    ROUND(AVG(num_lab_procedures), 2) AS avg_lab_procedures,
    ROUND(AVG(num_procedures), 2) AS avg_other_procedures
FROM diabetic_data
