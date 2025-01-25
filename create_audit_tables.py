# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import execute

def create_triggers():
    commands = (
        """
        CREATE OR REPLACE FUNCTION process_alumn_audit() RETURNS TRIGGER AS $alumn_audit$
            BEGIN
                IF (TG_OP = 'DELETE') THEN
                    INSERT INTO alumn_audit
                        SELECT 'D', now(), o.* FROM old_table o;
                ELSIF (TG_OP = 'UPDATE') THEN
                    INSERT INTO alumn_audit
                        SELECT 'U', now(), n.* FROM new_table n;
                ELSIF (TG_OP = 'INSERT') THEN
                    INSERT INTO alumn_audit
                        SELECT 'I', now(), n.* FROM new_table n;
                END IF;
                RETURN NULL; -- result is ignored since this is an AFTER trigger
            END;
        $alumn_audit$ LANGUAGE plpgsql;
        """,
        """
        CREATE TRIGGER alumn_audit_ins
            AFTER INSERT ON alumn
            REFERENCING NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_alumn_audit();
        CREATE TRIGGER alumn_audit_upd
            AFTER UPDATE ON alumn
            REFERENCING OLD TABLE AS old_table NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_alumn_audit();
        CREATE TRIGGER alumn_audit_del
            AFTER DELETE ON alumn
            REFERENCING OLD TABLE AS old_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_alumn_audit();
        """,
        """
        CREATE OR REPLACE FUNCTION process_teacher_audit() RETURNS TRIGGER AS $teacher_audit$
            BEGIN
                IF (TG_OP = 'DELETE') THEN
                    INSERT INTO teacher_audit
                        SELECT 'D', now(), o.* FROM old_table o;
                ELSIF (TG_OP = 'UPDATE') THEN
                    INSERT INTO teacher_audit
                        SELECT 'U', now(), n.* FROM new_table n;
                ELSIF (TG_OP = 'INSERT') THEN
                    INSERT INTO teacher_audit
                        SELECT 'I', now(), n.* FROM new_table n;
                END IF;
                RETURN NULL; -- result is ignored since this is an AFTER trigger
            END;
        $teacher_audit$ LANGUAGE plpgsql;
        """,
        """
        CREATE TRIGGER teacher_audit_ins
            AFTER INSERT ON teacher
            REFERENCING NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_teacher_audit();
        CREATE TRIGGER teacher_audit_upd
            AFTER UPDATE ON teacher
            REFERENCING OLD TABLE AS old_table NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_teacher_audit();
        CREATE TRIGGER teacher_audit_del
            AFTER DELETE ON teacher
            REFERENCING OLD TABLE AS old_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_teacher_audit();
        """,
        """
        CREATE OR REPLACE FUNCTION process_course_audit() RETURNS TRIGGER AS $course_audit$
            BEGIN
                IF (TG_OP = 'DELETE') THEN
                    INSERT INTO course_audit
                        SELECT 'D', now(), o.* FROM old_table o;
                ELSIF (TG_OP = 'UPDATE') THEN
                    INSERT INTO course_audit
                        SELECT 'U', now(), n.* FROM new_table n;
                ELSIF (TG_OP = 'INSERT') THEN
                    INSERT INTO course_audit
                        SELECT 'I', now(), n.* FROM new_table n;
                END IF;
                RETURN NULL; -- result is ignored since this is an AFTER trigger
            END;
        $course_audit$ LANGUAGE plpgsql;
        """,
        """
        CREATE TRIGGER course_audit_ins
            AFTER INSERT ON course
            REFERENCING NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_course_audit();
        CREATE TRIGGER course_audit_upd
            AFTER UPDATE ON course
            REFERENCING OLD TABLE AS old_table NEW TABLE AS new_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_course_audit();
        CREATE TRIGGER course_audit_del
            AFTER DELETE ON course
            REFERENCING OLD TABLE AS old_table
            FOR EACH STATEMENT EXECUTE FUNCTION process_course_audit();
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

    execute(commands, "audit.ini")

def create_tables():
    create_triggers()
    create_audit_tables