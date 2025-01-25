# Author 1: Álvaro Rivas Álvarez
# Autohr 2: Héctor de la Cruz Baquero

from flask import Flask, render_template, request, redirect, url_for
from insert import insert_user, insert_alumn, insert_teacher, insert_course
from delete import delete_alumn, delete_teacher, delete_course
from update import update_alumn, update_teacher, update_course
from select_ import select_various, select_one
from select_ import query_1_all, query_1_one, query_1_total
from select_ import query_2_all, query_2_one, query_2_total
from select_ import query_3_all, query_3_one, query_3_total
from search_elasticsearch import search_links_in_elasticsearch, elasticsearch_main
import mongo


rows = 10
alumn_page = 0
teacher_page = 0
course_page = 0
query_1_page = 0
query_2_page = 0
query_3_page = 0
logged = False
user = ''
# elasticsearch_main('https://www.ucjc.edu')
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/menu')
def menu():
    if not logged:
        mongo.insert('failed_login_attempt', '/menu', request.remote_addr, None)
        return redirect(url_for('login'))
    mongo.insert(user, '/menu', request.remote_addr, None)
    return render_template('menu.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if not logged:
        mongo.insert('failed_login_attempt', '/search', request.remote_addr, None)
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        keyword = request.form['search']
        search_results = search_links_in_elasticsearch(keyword)
        mongo.insert(user, '/search_elasticsearch', request.remote_addr, keyword)
        return render_template('search.html', search_results=search_results)
    
    mongo.insert(user, '/search', request.remote_addr, None)
    return render_template('search.html')

@app.route('/university')
def university():
    if not logged:
        mongo.insert('failed_login_attempt', '/university', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/university', request.remote_addr, None)
    return render_template('university.html')

@app.route('/queries')
def queries():
    if not logged:
        mongo.insert('failed_login_attempt', '/queries', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/queries', request.remote_addr, None)
    return render_template('queries.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/query_1')
def query_1():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_1', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = query_1_all(rows, query_1_page)
    query_1_data = select_various(sql, 'main.ini')
    total = select_one(query_1_total(), 'main.ini')
    total_pages= total // rows
    page = (query_1_page // rows) + 1
    mongo.insert(user, '/query_1', request.remote_addr, None)
    return render_template('query_1.html', query_1_data=query_1_data, total=total, total_pages=total_pages, page=page, search=False)

@app.route('/query_1_previous')
def query_1_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_1_previous', request.remote_addr)
        return redirect(url_for('login'))
    
    global query_1_page
    if query_1_page == 0:
        return redirect(url_for('query_1'))
    query_1_page -= rows
    mongo.insert(user, '/query_1_previous', request.remote_addr, None)
    return redirect(url_for('query_1'))

@app.route('/query_1_next')
def query_1_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_1_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global query_1_page
    query_1_page += rows
    mongo.insert(user, '/query_1_next', request.remote_addr, None)
    return redirect(url_for('query_1'))

@app.route('/search_query_1', methods=['GET', 'POST'])
def search_query_1():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_query_1', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    sql = query_1_one(name)
    query_1_data = select_various(sql, 'main.ini')
    mongo.insert(user, '/search_query_1', request.remote_addr, name)
    return render_template('query_1.html', query_1_data=query_1_data, search=True)

@app.route('/query_2')
def query_2():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_2', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = query_2_all(rows, query_2_page)
    query_2_data = select_various(sql, 'main.ini')
    total = select_one(query_2_total(), 'main.ini')
    total_pages= total // rows
    page = (query_2_page // rows) + 1
    mongo.insert(user, '/query_2', request.remote_addr, None)
    return render_template('query_2.html', query_2_data=query_2_data, total=total, total_pages=total_pages, page=page, search=False)

@app.route('/query_2_previous')
def query_2_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_2_previous', request.remote_addr)
        return redirect(url_for('login'))
    
    global query_2_page
    if query_2_page == 0:
        return redirect(url_for('query_2'))
    query_2_page -= rows
    mongo.insert(user, '/query_2_previous', request.remote_addr, None)
    return redirect(url_for('query_2'))

@app.route('/query_2_next')
def query_2_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_2_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global query_2_page
    query_2_page += rows
    mongo.insert(user, '/query_2_next', request.remote_addr, None)
    return redirect(url_for('query_2'))

@app.route('/search_query_2', methods=['GET', 'POST'])
def search_query_2():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_query_2', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    sql = query_2_one(name)
    query_2_data = select_various(sql, 'main.ini')
    mongo.insert(user, '/search_query_2', request.remote_addr, name)
    return render_template('query_2.html', query_2_data=query_2_data, search=True)

@app.route('/query_3')
def query_3():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_3', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = query_3_all(rows, query_3_page)
    query_3_data = select_various(sql, 'main.ini')
    total = select_one(query_3_total(), 'main.ini')
    total_pages= total // rows
    page = (query_3_page // rows) + 1
    mongo.insert(user, '/query_3', request.remote_addr, None)
    return render_template('query_3.html', query_3_data=query_3_data, total=total, total_pages=total_pages, page=page, search=False)

@app.route('/query_3_previous')
def query_3_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_3_previous', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global query_3_page
    if query_3_page == 0:
        return redirect(url_for('query_3'))
    query_3_page -= rows
    mongo.insert(user, '/query_3_previous', request.remote_addr, None)
    return redirect(url_for('query_3'))

@app.route('/query_3_next')
def query_3_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/query_3_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global query_3_page
    query_3_page += rows
    mongo.insert(user, '/query_3_next', request.remote_addr, None)
    return redirect(url_for('query_3'))

@app.route('/search_query_3', methods=['GET', 'POST'])
def search_query_3():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_query_3', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    sql = query_3_one(name)
    query_3_data = select_various(sql, 'main.ini')
    mongo.insert(user, '/search_query_3', request.remote_addr, name)
    return render_template('query_3.html', query_3_data=query_3_data, search=True)

@app.route('/alumns')
def alumns():
    if not logged:
        mongo.insert('failed_login_attempt', '/alumns', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = "SELECT * FROM alumn ORDER BY id LIMIT %s OFFSET %s" % (rows, alumn_page)
    alumn_data = select_various(sql, 'main.ini')
    total = "SELECT COUNT(*) FROM alumn"
    total_data = select_one(total, 'main.ini')
    total_pages= total_data // rows
    page = (alumn_page // rows) + 1
    mongo.insert(user, '/alumns', request.remote_addr, None)
    return render_template('alumns.html', alumn_data=alumn_data, total=total_data, total_pages=total_pages, page=page, search=False)

@app.route('/alumn_previous')
def alumn_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/alumn_previous', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global alumn_page
    if alumn_page == 0:
        return redirect(url_for('alumns'))
    alumn_page -= rows
    mongo.insert(user, '/alumn_previous', request.remote_addr, None)
    return redirect(url_for('alumns'))

@app.route('/alumn_next')
def alumn_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/alumn_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global alumn_page
    alumn_page += rows
    mongo.insert(user, '/alumn_next', request.remote_addr, None)
    return redirect(url_for('alumns'))

@app.route('/search_alumn', methods=['GET', 'POST'])
def search_alumn():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_alumn', request.remote_addr, None)
        return redirect(url_for('login'))
    
    keyword = request.form['keyword']
    if keyword.isdigit():
        sql = "SELECT * FROM alumn WHERE id = %s" % keyword
    else:
        sql = "SELECT * FROM alumn WHERE name ILIKE '%s' OR email ILIKE '%s' OR address ILIKE '%s' ORDER BY id" % (keyword, keyword, keyword)
    
    mongo.insert(user, '/search_alumn', request.remote_addr, keyword)
    return render_template('alumns.html', alumn_data=select_various(sql, 'main.ini'), search=True)

@app.route('/teachers')
def teachers():
    if not logged:
        mongo.insert('failed_login_attempt', '/teachers', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = "SELECT * FROM teacher ORDER BY id LIMIT %s OFFSET %s" % (rows, teacher_page)
    teacher_data = select_various(sql, 'main.ini')
    total = "SELECT COUNT(*) FROM teacher"
    total_data = select_one(total, 'main.ini')
    total_pages= total_data // rows
    page = (teacher_page // rows) + 1
    mongo.insert(user, '/teachers', request.remote_addr, None)
    return render_template('teachers.html', teacher_data=teacher_data, total=total_data, total_pages=total_pages, page=page, search=False)

@app.route('/teacher_previous')
def teacher_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/teacher_previous', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global teacher_page
    if teacher_page == 0:
        return redirect(url_for('teachers'))
    teacher_page -= rows
    mongo.insert(user, '/teacher_previous', request.remote_addr, None)
    return redirect(url_for('teachers'))

@app.route('/teacher_next')
def teacher_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/teacher_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global teacher_page
    teacher_page += rows
    mongo.insert(user, '/teacher_previous', request.remote_addr, None)
    return redirect(url_for('teachers'))

@app.route('/search_teacher', methods=['GET', 'POST'])
def search_teacher():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_teacher', request.remote_addr, None)
        return redirect(url_for('login'))
    
    keyword = request.form['keyword']
    if keyword.isdigit():
        sql = "SELECT * FROM teacher WHERE id = %s" % keyword
    else:
        sql = "SELECT * FROM teacher WHERE name ILIKE '%s' OR email ILIKE '%s' ORDER BY id" % (keyword, keyword)
    
    mongo.insert(user, '/search_teacher', request.remote_addr, keyword)
    return render_template('teachers.html', teacher_data=select_various(sql, 'main.ini'), search=True)

@app.route('/courses')
def courses():
    if not logged:
        mongo.insert('failed_login_attempt', '/courses', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = """
        SELECT course.id, course.name, teacher.name
        FROM course
        JOIN teacher ON course.teacher_id = teacher.id
        ORDER BY id LIMIT %s OFFSET %s
        """ % (rows, course_page)

    course_data = select_various(sql, 'main.ini')
    total = "SELECT COUNT(*) FROM course"
    total_data = select_one(total, 'main.ini')
    total_pages= total_data // rows
    page = (course_page // rows) + 1
    mongo.insert(user, '/courses', request.remote_addr, None)
    return render_template('courses.html', course_data=course_data, total=total_data, total_pages=total_pages, page=page, search=False)

@app.route('/course_previous')
def course_previous():
    if not logged:
        mongo.insert('failed_login_attempt', '/course_previous', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global course_page
    if course_page == 0:
        return redirect(url_for('courses'))
    course_page -= rows
    mongo.insert(user, '/course_previous', request.remote_addr, None)
    return redirect(url_for('courses'))

@app.route('/course_next')
def course_next():
    if not logged:
        mongo.insert('failed_login_attempt', '/course_next', request.remote_addr, None)
        return redirect(url_for('login'))
    
    global course_page
    course_page += rows
    mongo.insert(user, '/course_next', request.remote_addr, None)
    return redirect(url_for('courses'))

@app.route('/search_course', methods=['GET', 'POST'])
def search_course():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_course', request.remote_addr, None)
        return redirect(url_for('login'))
    
    keyword = request.form['keyword']
    if keyword.isdigit():
        sql = """
            SELECT course.id, course.name, teacher.name
            FROM course
            JOIN teacher ON course.teacher_id = teacher.id
            WHERE course.id = %s
            """ % keyword
    else:
        sql = """
            SELECT course.id, course.name, teacher.name
            FROM course
            JOIN teacher ON course.teacher_id = teacher.id
            WHERE course.name ILIKE '%s'
            OR teacher.name ILIKE '%s'
            ORDER BY course.id
            """ % (keyword, keyword)

    mongo.insert(user, '/search_course', request.remote_addr, keyword)
    return render_template('courses.html', course_data=select_various(sql, 'main.ini'), search=True)

@app.route('/insert_alumn_interface')
def insert_alumn_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_alumn_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/insert_alumn_interface', request.remote_addr, None)
    return render_template('insert_alumn.html')

@app.route('/insert_new_alumn', methods=['GET', 'POST'])
def insert_new_alumn():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_new_alumn', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    insert_alumn(name, email, address)

    args = {
        "name": name,
        "email": email,
        "address": address
    }

    mongo.insert(user, '/insert_new_alumn', request.remote_addr, args)
    return redirect(url_for('alumns'))

@app.route('/insert_teacher_interface')
def insert_teacher_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_teacher_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/insert_teacher_interface', request.remote_addr, None)
    return render_template('insert_teacher.html')

@app.route('/insert_new_teacher', methods=['GET', 'POST'])
def insert_new_teacher():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_new_teacher', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    email = request.form['email']
    insert_teacher(name, email)

    args = {
        "name": name,
        "email": email
    }

    mongo.insert(user, '/insert_new_teacher', request.remote_addr, args)
    return redirect(url_for('teachers'))

@app.route('/insert_course_interface')
def insert_course_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_course_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/insert_course_interface', request.remote_addr, None)
    return render_template('insert_course.html')

@app.route('/insert_new_course', methods=['GET', 'POST'])
def insert_new_course():
    if not logged:
        mongo.insert('failed_login_attempt', '/insert_course_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    name = request.form['name']
    teacher_id = request.form['teacher_id']
    insert_course(name, teacher_id)

    args = {
        "name": name,
        "teacher_id": teacher_id
    }

    mongo.insert(user, '/insert_new_course', request.remote_addr, args)
    return redirect(url_for('courses'))

@app.route('/insert_user', methods=['GET', 'POST'])
def insert_new_user():
    username = request.form['username']
    password = request.form['password']
    insert_user(username, password)
    mongo.insert(username, '/insert_new_user', request.remote_addr, username)
    return redirect(url_for('login'))

@app.route('/update_alumn_interface', methods=['GET', 'POST'])
def update_alumn_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_alumn_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['alumn_id']
    mongo.insert(user, '/update_alumn_interface', request.remote_addr, None)
    return render_template('update_alumn.html', id=id)

@app.route('/update_alumn', methods=['GET', 'POST'])
def update_one_alumn():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_alumn', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['alumn_id']
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    update_alumn(id, name, email, address)

    args = {
        "id": id,
        "name": name,
        "email": email,
        "address": address
    }

    mongo.insert(user, '/update_alumn', request.remote_addr, args)
    return redirect(url_for('alumns'))

@app.route('/update_teacher_interface', methods=['GET', 'POST'])
def update_teacher_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_alumn', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['teacher_id']
    mongo.insert(user, '/update_teacher_interface', request.remote_addr, None)
    return render_template('update_teacher.html', id=id)

@app.route('/update_teacher', methods=['GET', 'POST'])
def update_one_teacher():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_teacher', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['teacher_id']
    name = request.form['name']
    email = request.form['email']
    update_teacher(id, name, email)

    args = {
        "id": id,
        "name": name,
        "email": email
    }

    mongo.insert(user, '/update_teacher', request.remote_addr, args)
    return redirect(url_for('teachers'))

@app.route('/update_course_interface', methods=['GET', 'POST'])
def update_course_interface():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_course_interface', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['course_id']
    mongo.insert(user, '/update_course_interface', request.remote_addr, None)
    return render_template('update_course.html', id=id)

@app.route('/update_course', methods=['GET', 'POST'])
def update_one_course():
    if not logged:
        mongo.insert('failed_login_attempt', '/update_course', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['course_id']
    name = request.form['name']
    teacher_id = request.form['teacher_id']
    update_course(id, name, teacher_id)

    args = {
        "id": id,
        "name": name,
        "teacher_id": teacher_id
    }

    mongo.insert(user, '/update_course', request.remote_addr, args)
    return redirect(url_for('courses'))

@app.route('/delete_alumn', methods=['GET', 'POST'])
def delete_one_alumn():
    if not logged:
        mongo.insert('failed_login_attempt', '/delete_alumn', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['alumn_id']
    delete_alumn(id)
    mongo.insert(user, '/delete_alumn', request.remote_addr, id)
    return redirect(url_for('alumns'))

@app.route('/delete_teacher', methods=['GET', 'POST'])
def delete_one_teacher():
    if not logged:
        mongo.insert('failed_login_attempt', '/delete_teacher', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['teacher_id']
    delete_teacher(id)
    mongo.insert(user, '/delete_teacher', request.remote_addr, id)
    return redirect(url_for('teachers'))

@app.route('/delete_course', methods=['GET', 'POST'])
def delete_one_course():
    if not logged:
        mongo.insert('failed_login_attempt', '/delete_course', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['course_id']
    delete_course(id)
    mongo.insert(user, '/delete_course', request.remote_addr, id)
    return redirect(url_for('courses'))

@app.route('/audit')
def audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/audit', request.remote_addr, None)
        return redirect(url_for('login'))
    
    mongo.insert(user, '/audit', request.remote_addr, None)
    return render_template('audit.html')

@app.route('/alumn_audit')
def alumn_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/alumn_audit', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = "SELECT * FROM alumn_audit ORDER BY id"
    mongo.insert(user, '/alumn_audit', request.remote_addr, None)
    return render_template('alumn_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/search_alumn_audit', methods=['GET', 'POST'])
def search_alumn_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_alumn_audit', request.remote_addr, None)
        return redirect(url_for('login'))
    
    id = request.form['alumn_id']
    sql = "SELECT * FROM alumn_audit WHERE id = %s" % id
    mongo.insert(user, '/search_alumn_audit', request.remote_addr, id)
    return render_template('alumn_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/teacher_audit')
def teacher_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/teacher_audit', request.remote_addr, None)
        return redirect(url_for('login'))
    
    sql = "SELECT * FROM teacher_audit ORDER BY id"
    mongo.insert(user, '/teacher_audit', request.remote_addr, None)
    return render_template('teacher_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/search_teacher_audit', methods=['GET', 'POST'])
def search_teacher_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_teacher_audit', request.remote_addr), None
        return redirect(url_for('login'))
    
    id = request.form['teacher_id']
    sql = "SELECT * FROM teacher_audit WHERE id = %s" % id
    mongo.insert(user, '/search_teacher_audit', request.remote_addr, id)
    return render_template('teacher_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/course_audit')
def course_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/course_audit', request.remote_addr, None)
        return redirect(url_for('login'))
    sql = "SELECT * FROM course_audit ORDER BY id"
    mongo.insert(user, '/course_audit', request.remote_addr, None)
    return render_template('course_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/search_course_audit', methods=['GET', 'POST'])
def search_course_audit():
    if not logged:
        mongo.insert('failed_login_attempt', '/search_course_audit', request.remote_addr, None)
        return redirect(url_for('login'))
    id = request.form['course_id']
    sql = "SELECT * FROM course_audit WHERE id = %s" % id
    mongo.insert(user, '/search_course_audit', request.remote_addr, id)
    return render_template('course_audit.html', data=select_various(sql, 'main.ini'))

@app.route('/check_login', methods=['GET', 'POST'])
def check_login():
    username = request.form['username']
    password = request.form['password']
    sql = "SELECT password FROM username WHERE username = '%s'" % (username)
    password1 = select_one(sql, "main.ini")
    sql = ("SELECT md5('%s')" % password)
    password2 = select_one(sql, "main.ini")
    
    if password1 != password2:
        mongo.insert('failed_login_attemp', '/check_login', request.remote_addr, username)
        return redirect(url_for('login'))
    
    global logged
    logged = True
    global user
    user = username

    mongo.insert(username, '/check_login', request.remote_addr, username)
    return redirect(url_for('menu'))

def run_app():
    app.run(debug=True)

if __name__ == '__main__':
    run_app()