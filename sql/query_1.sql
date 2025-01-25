SELECT
    t.id AS teacher_id,
    t.name AS teacher_name,
    COUNT(DISTINCT car.alumn_id) AS num_alumns,
    COUNT(DISTINCT c.id) AS num_courses
FROM
    teacher t
LEFT JOIN
    course c ON t.id = c.teacher_id
LEFT JOIN
    course_alumn_rel car ON c.id = car.course_id
WHERE
    t.name LIKE '<TEACHER_NAME>'
GROUP BY
    t.id, t.name;