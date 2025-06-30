import sqlite3
conn = sqlite3.connect("shopping.db")
cursor = conn.cursor()




cursor.execute ('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL)''')


cursor.execute ('''CREATE TABLE IF NOT EXISTS customers ( 
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE''')

cursor.execute ('''CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)''')

while True:
    print("1 - Додавання продуктів:")
    print("2 - Додавання клієнтів")
    print("3 - Замовлення товарів:")
    print("4 - Сумарний обсяг продажів:")
    print("5 - Кількість замовлень на кожного клієнта:")
    print("6 - Середній чек замовлення:")
    print("7 - Найбільш популярна категорія товарів:")
    print("8 - Загальна кількість товарів кожної категорії:")
    print("9 - Оновлення цін:")
    print("10 - Вихід")

    shop = input()
    if  shop == "1":
        name = input("ведіть назву продукту: ")
        category = input("Ведіть категорію товару: ")
        price = float(input("Ведіть ціну товару: "))
        cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        conn. commit()

    elif shop == "2":
        first_name = input("ведіть ім'я клієнта: ")
        last_name = input("Ведіть  прізвище клієнта: ")
        email = input("Ведіть електронну пошту клієнта: ")
        cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
        conn. commit()

    elif shop == "3":
        customer_id = int(input("Ведіть id покупця: "))
        product_id = int(input("Ведіть ід продукту: " ))
        quantity = int(input("Ведіть кількість товару: "))
        order_data = input("Ведіть дату замовлення (рік - місяць - день): ")
        cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)", (customer_id, product_id, quantity, order_data))
        conn.commit()
    elif shop == "4":
        cursor.execute("SELECT SUM(orders.quantity * products.price) AS total_sales FROM orders JOIN products ON orders.product_id = products.product_id")
        total_sales = cursor.fetchone()[0]
        print(f"Сумарний обсяг продажів: {total_sales if total_sales else 0} грн")

