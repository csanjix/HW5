import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.executemany('INSERT INTO countries (title) VALUES (?)', [('USA',), ('UK',), ('France',)])

cursor.execute('''
    CREATE TABLE cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

cities_data = [
    ('New York', 468.9, 1),
    ('London', 607, 2),
    ('Paris', 105.4, 3),
    ('Berlin', 891.8, 3),
    ('Beijing', 16410.54, 4),
    ('Moscow', 2511, 5),
    ('Tokyo', 2188.21, 6)
]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities_data)

cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

# 6. Добавляем 15 сотрудников в разных городах
employees_data = [
    ('John', 'Doe', 1),
    ('Alice', 'Smith', 1),
    ('Bob', 'Johnson', 2),
    ('Eva', 'Brown', 2),
    ('Michael', 'Lee', 3),
    ('Sarah', 'White', 3),
    ('David', 'Miller', 4),
    ('Linda', 'Davis', 4),
    ('Alex', 'Wilson', 5),
    ('Olivia', 'Jones', 5),
    ('James', 'Martin', 6),
    ('Emily', 'Taylor', 6),
    ('Daniel', 'Anderson', 7),
    ('Emma', 'Moore', 7),
    ('William', 'Harris', 7)
]
cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)', employees_data)

conn.commit()
conn.close()

while True:
    try:
        city_id = int(input("Введите id города (0 для выхода): "))
        if city_id == 0:
            break
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT employees.first_name, employees.last_name, cities.title, countries.title, cities.area
            FROM employees
            INNER JOIN cities ON employees.city_id = cities.id
            INNER JOIN countries ON cities.country_id = countries.id
            WHERE employees.city_id = ?
        ''', (city_id,))
        employees = cursor.fetchall()
        if not employees:
            print("Сотрудники для выбранного города не найдены.")
        else:
            print("Имя  Фамилия  Город  Страна  Площадь города")
            for employee in employees:
                print(f"{employee[0]}  {employee[1]}  {employee[2]}  {employee[3]}  {employee[4]}")
        conn.close()
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")