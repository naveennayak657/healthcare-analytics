SELECT 
    race,
    ROUND(AVG(num_medications), 2) AS avg_medications
FROM diabetic_data
GROUP BY race
ORDER BY avg_medications DESC
