# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import load_config
import psycopg2

def select_various(command, database):
    try:
        config = load_config(database)
        with psycopg2.connect(**config) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(command)
                return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def select_one(command, database):
    try:
        config = load_config(database)
        with psycopg2.connect(**config) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(command)
                return cur.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def query_1_total():
    return """
        SELECT
            COUNT(*) AS total_results
        FROM
            (SELECT
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
            GROUP BY
                t.id, t.name) AS subquery;
    """

def query_1_all(rows, query_1_page):
    return """
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
        GROUP BY
            t.id, t.name
        LIMIT %s OFFSET %s;
    """ % (rows, query_1_page)

def query_1_one(name):
    return """
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
            t.name ILIKE '%s'
        GROUP BY
            t.id, t.name;
    """ % name

def query_2_total():
    return """
        SELECT
            COUNT(*) AS total_results
        FROM
            (SELECT
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
                alumn a ON car.alumn_id = a.id) AS subquery;
    """

def query_2_one(name):
    return """
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
            alumn a ON car.alumn_id = a.id
        WHERE c.name ILIKE '%s';
    """ % name

def query_2_all(rows, query_2_page):
    return """
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
            alumn a ON car.alumn_id = a.id
        LIMIT %s OFFSET %s;
    """ % (rows, query_2_page)

def query_3_total():
    return """
    SELECT
        COUNT(*) AS total_results
    FROM
        (SELECT
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
        GROUP BY
            a.id, a.name) AS subquery;
    """

def query_3_all(rows, query_3_page):
    return """
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
        GROUP BY
            a.id, a.name
        LIMIT %s OFFSET %s;
    """ % (rows, query_3_page)

def query_3_one(name):
    return """
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
            a.name ILIKE '%s'
        GROUP BY
            a.id, a.name;
    """ % name