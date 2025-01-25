SELECT
    c.id AS course_id,
    c.name AS course_name,
    a.id AS alumn_id,
    a.name AS alumn_name,
    t.id AS teacher_id,
    t.name AS teacher_name
FROM
    course c
LEFT JOIN
    teacher t ON c.teacher_id = t.id
LEFT JOIN
    course_alumn_rel car ON c.id = car.course_id
LEFT JOIN
    alumn a ON car.alumn_id = a.id;