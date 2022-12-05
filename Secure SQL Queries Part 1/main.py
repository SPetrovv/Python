import sqlite3

conn = sqlite3.connect("customers.db")

cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS customers;""")

cursor.execute("""CREATE TABLE customers (
    name VARCHAR(255) NOT NULL,
    job VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    age INT,
    gender  CHAR(1)); """)

cursor.execute("""INSERT INTO customers (name,job, password, age, gender) VALUES 
('Mike', 'Programmer', 'password', 45, 'm'),
('John', 'Builder', '123456', 35, 'm');
 """)

conn.commit()

age_input = input("Enter an age: ")

cursor.execute(f"SELECT * FROM customers WHERE age > {age_input}")

# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)

name_input = input("What is your username: ")
password_input = input("What is your password: ")

cursor.execute(F"SELECT * FROM customers WHERE name = ? AND password = ?", (name_input, password_input))

rows = cursor.fetchall()
if len(rows) == 0:
    print("Login Failed!")
else:
    print("Success! Here is the information:")
    for row in rows:
        print(row)
