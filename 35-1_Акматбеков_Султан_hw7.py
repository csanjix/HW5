import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def create_products(conn):
    create_product(conn, ('Agusha', 52.5, 100))
    create_product(conn, ('Lays', 52.5, 100))
    create_product(conn, ('Mojito', 52.5, 100))
    create_product(conn, ('Nitro', 52.5, 100))
    create_product(conn, ('Flash', 52.5, 100))
    create_product(conn, ('Huggies', 52.5, 100))
    create_product(conn, ('Russkaya kartoshka', 52.5, 100))
    create_product(conn, ('Cookies', 52.5, 100))
    create_product(conn, ('Candies', 52.5, 100))
    create_product(conn, ('Marshmallow', 52.5, 100))
    create_product(conn, ('Tomatoes', 52.5, 100))
    create_product(conn, ('Cucumber', 52.5, 100))
    create_product(conn, ('Potato', 52.5, 100))
    create_product(conn, ('Carrot', 52.5, 100))
    create_product(conn, ('Watermelon', 52.5, 100))


def update_product_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_product_price(conn, product: tuple):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_product_by_id(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def print_products_by_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE quantity > 5 AND price < 100.0'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def print_all_product_by_title(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ("%"+word+"%",))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


connection = create_connection(db_name='hw.db')

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print_all_product_by_title(connection, 'Nitro')