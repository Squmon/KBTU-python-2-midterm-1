SELECT *
FROM students
WHERE 
    (fullname = :name OR :name IS NULL)
    AND 
    (id = :id OR :id IS NULL);
