# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import execute

def delete_alumn(id):
    sql = ("DELETE FROM alumn WHERE id = %s" % id,)
    execute(sql, "main.ini")

def delete_teacher(id):
    sql = ("DELETE FROM teacher WHERE id = %s" % id,)
    execute(sql, "main.ini")

def delete_course(id):
    sql = ("DELETE FROM course WHERE id = %s" % id,)
    execute(sql, "main.ini")

def delete_all_alumns():
    sql = ("DELETE FROM alumn",)
    execute(sql, "main.ini")

def delete_all_teachers():
    sql = ("DELETE FROM teacher",)
    execute(sql, "main.ini")

def delete_all_courses():
    sql = ("DELETE FROM course",)
    execute(sql, "main.ini")

def delete_all():
    delete_all_alumns()
    delete_all_teachers()
    delete_all_courses()