-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month > 6 AND month < 9
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
