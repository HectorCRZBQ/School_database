SELECT
    a.id AS alumn_id,
    a.name AS alumn_name,
    COUNT(DISTINCT c.id) AS num_courses,
    COUNT(DISTINCT t.id) AS num_teachers
FROM 
    alumn a
LEFT JOIN
    course_alumn_rel car ON a.id = car.alumn_id
LEFT JOIN
    course c ON car.course_id = c.id
LEFT JOIN
    teacher t ON c.teacher_id = t.id
WHERE
    a.name LIKE '<ALUMN_NAME>'
GROUP BY
    a.id, a.name;