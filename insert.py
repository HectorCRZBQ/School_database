# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import execute
from faker import Faker
import random

num_courses = 150
num_alumns = 1000
num_teachers = 10
alumns_per_course = 50

fake = Faker('es_ES')

def insert_alumn(name, email, address):
    sql = ("INSERT INTO alumn (name, email, address) VALUES ('%s', '%s', '%s')" % (name, email, address),)
    execute(sql, "main.ini")

def insert_teacher(name, email):
    sql = ("INSERT INTO teacher (name, email) VALUES ('%s', '%s')" % (name, email),)
    execute(sql, "main.ini")

def insert_course(name, teacher_id):
    sql = ("INSERT INTO course (name, teacher_id) VALUES ('%s', '%s')" % (name, teacher_id),)
    execute(sql, "main.ini")

def insert_course_alumn_rel(alumn_id, course_id):
    sql = ("INSERT INTO course_alumn_rel (alumn_id, course_id) VALUES ('%s', '%s')" % (alumn_id, course_id),)
    execute(sql, "main.ini")

def insert_user(username, password):
    sql = ("INSERT INTO username (username, password) VALUES ('%s', md5('%s'))" % (username, password),)
    execute(sql, "main.ini")

def insert_many_alumns():
    for _ in range(num_alumns):
        insert_alumn(fake.name(), fake.email(), fake.address())

def insert_many_teachers():
    for _ in range(num_teachers):
        insert_teacher(fake.name(), fake.email())

def insert_many_courses():
    for course_id in range(num_courses):
        insert_course(fake.word(), random.randint(1, num_teachers))
        alumns = set()

        while len(alumns) < alumns_per_course:
            alumn_id = random.randint(1, num_alumns)
            alumns.add(alumn_id)

        for alumn_id in alumns:
            insert_course_alumn_rel(alumn_id, course_id + 1)

def insert_all():
    insert_many_alumns()
    insert_many_teachers()
    insert_many_courses()

if __name__ == '__main__':
    insert_all()