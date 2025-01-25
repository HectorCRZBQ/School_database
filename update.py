# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from config import execute

def update_alumn(id, name=None, email=None, address=None):
    values = []
    if name != "":
        values.append("name = '%s'" % name)
    if email != "":
        values.append("email = '%s'" % email)
    if address != "":
        values.append("address = '%s'" % address)

    if not values:
        return

    clause = ", ".join(values)
    sql = ("UPDATE alumn SET %s WHERE id = %s" % (clause, id),)
    execute(sql, "main.ini")

def update_teacher(id, name=None, email=None):
    values = []
    if name != "":
        values.append("name = '%s'" % name)
    if email != "":
        values.append("email = '%s'" % email)

    if not values:
        return

    clause = ", ".join(values)
    sql = ("UPDATE teacher SET %s WHERE id = %s" % (clause, id),)
    execute(sql, "main.ini")

def update_course(id, name=None, teacher_id=None):
    values = []
    if name != "":
        values.append("name = '%s'" % name)
    if teacher_id != "":
        values.append("teacher_id = '%s'" % teacher_id)

    if not values:
        return

    clause = ", ".join(values)
    sql = ("UPDATE course SET %s WHERE id = %s" % (clause, id),)
    execute(sql, "main.ini")