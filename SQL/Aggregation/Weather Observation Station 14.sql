/*
Enter your query here.
*/
SELECT TRUNCATE(LAT_N, 4)
FROM STATION
WHERE LAT_N IN (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);