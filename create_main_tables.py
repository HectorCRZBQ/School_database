# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import execute

def create_main_tables():
    commands = (
        """
        CREATE TABLE alumn (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            address VARCHAR
        )
        """,
        """
        CREATE TABLE teacher (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE course (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            teacher_id INT NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE course_alumn_rel (
            alumn_id INT NOT NULL,
            course_id INT NOT NULL,
            PRIMARY KEY (alumn_id, course_id),
            FOREIGN KEY (alumn_id) REFERENCES alumn(id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE username (
            username VARCHAR PRIMARY KEY,
            password VARCHAR NOT NULL
        )
        """
    )

    execute(commands, "main.ini")

def create_main_index():
    commands = (
        """
        CREATE INDEX alumn_index ON alumn(name)
        """,
        """
        CREATE INDEX teacher_index ON teacher(name)
        """,
        """
        CREATE INDEX course_index ON course(name)
        """,
        """
        CREATE INDEX course_alumn_rel_index ON course_alumn_rel(alumn_id, course_id)
        """
    )

    execute(commands, "main.ini")

def create_audit_tables():
    commands = (
        """
        CREATE TABLE alumn_audit (
            operation CHAR(1) NOT NULL,
            stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            id INT,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            address VARCHAR
        )
        """,
        """
        CREATE TABLE teacher_audit (
            operation CHAR(1) NOT NULL,
            stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            id INT,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE course_audit (
            operation CHAR(1) NOT NULL,
            stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            id INT,
            name VARCHAR NOT NULL,
            teacher_id INT NOT NULL
        )
        """
    )

    execute(commands, "main.ini")

def create_tables():
    create_main_tables()
    create_main_index()
    create_audit_tables()