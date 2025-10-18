SELECT
    id,
    fullname,
    Math,
    Physics,
    DuckScience,
    ICT,
    English,
    ROUND((Math + Physics + DuckScience + ICT + English)/5.0, 2) AS Average,
    CASE
        WHEN (Math + Physics + DuckScience + ICT + English)/5.0 >= 90 THEN 'A'
        WHEN (Math + Physics + DuckScience + ICT + English)/5.0 >= 80 THEN 'B'
        WHEN (Math + Physics + DuckScience + ICT + English)/5.0 >= 70 THEN 'C'
        WHEN (Math + Physics + DuckScience + ICT + English)/5.0 >= 60 THEN 'D'
        WHEN (Math + Physics + DuckScience + ICT + English)/5.0 >= 50 THEN 'E'
        ELSE 'F'
    END AS Grade
FROM students
WHERE 
    (fullname = :name OR :name IS NULL)
    AND 
    (id = :id OR :id IS NULL);
