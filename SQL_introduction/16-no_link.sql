-- Lists all records from second_table with a non-empty name
-- Display score and name ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
AND name != ''
ORDER BY score DESC;
