import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT
               )
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instructor TEXT)
               ''')
cursor.execute("CREATE TABLE IF NOT EXISTS student_courses (student_id INTEGER,course_id INTEGER,FOREIGN KEY (student_id) REFERENCES students(id),FOREIGN KEY (course_id) REFERENCES courses(course_id)PRIMARY KEY (student_id, course_id))")

while True:
    print("1. Додати студента")
    print("2. Додати курс")
    print("3. показати студентів")
    print("4. Показати курси")
    print("5. зареєструвати студента на курс")
    print("6. показати студентів на курс")
    print("7. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        name = input("ведіть імя")
        age = int(input("Введіть вік: "))
        major = input("Введіть спеціальність: ")
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        conn.commit()
    elif choice == '2':
        course_name = input("Введіть назву курсу: ")
        instructor = input("Введіть прізвище викладача: ")
        cursor.execute('INSERT INTO courses (course_name, instructor) VALUES (?, ?)', (course_name, instructor))
        conn.commit()
    elif choice == '3':
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()


        if not students:
                print("Немає студентів.")
        else:
            print("список студентів:")
            for s in students:
                print(f"ID: {s[0]}, Ім'я: {s[1]}, Вік: {s[2]}, Спеціальність: {s[3]}")

    elif choice == '4':
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
    
        if not courses:
            print("Немає курсів.")
        else:
            print("Список курсів:")
            for c in courses:
                print(f"ID: {c[0]}, Назва: {c[1]}, Викладач: {c[2]}")

    elif choice == '5':
        st_id = int(input("ведіть студента ID:"))
        c_id = int(input("ведіть курст ID:"))

        cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (st_id, c_id))
        conn.commit()
    elif choice == '6':
        course_id = int(input("Введіть ID курсу: "))
        cursor.execute(''' 
                        SELECT students.id, students.name, students.age, students.major
                        FROM students, student_courses
                        WHERE students.id = student_courses.student_id
                        AND student_courses.course_id = ?
                        ''', (course_id,))
        student_on_course = cursor.fetchall()
        if not student_on_course:
            print("Немає студентів на цьому курсі.")
        else:
            print("Студенти на курсі:")
            for s in student_on_course:
                print(f"ID: {s[0]}, Ім'я: {s[1]}, Вік: {s[2]}, Спеціальність: {s[3]}")

    elif choice == '7':
        break
    else:
        print("НЕПРАВИЛЬНО ВЕЛИ ЦИФРУ ВИБЕРІТЬ ІНШУ ЦИФРУ ВІД 1 ДО 7")

conn.close()