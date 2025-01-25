# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from configparser import ConfigParser
import psycopg2

def load_config(filename):
    section='postgresql'
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section %s not found in the %s file' % (section, filename))

    return config

def execute(commands, database):
    try:
        config = load_config(database)
        with psycopg2.connect(**config) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_database(database):
    config = load_config('postgres.ini')
    conn = psycopg2.connect(**config)
    conn.autocommit = True
    cursor = conn.cursor()
    sql = 'CREATE DATABASE %s;' % database
    cursor.execute(sql)
    conn.close()

def delete_database(database):
    config = load_config('postgres.ini')
    conn = psycopg2.connect(**config)
    conn.autocommit = True
    cursor = conn.cursor()
    sql = 'DROP DATABASE %s;' % database
    cursor.execute(sql)
    conn.close()