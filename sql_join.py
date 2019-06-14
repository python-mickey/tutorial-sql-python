import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sql_python_tutorial"
    )
    return mydb
def create_table_users():
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
def create_table_products():
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
def add_coloums_in_many_users():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (id, name, fav) VALUES (%s, %s, %s)"
    val = [
        { 1, 'John',  154},
        { 2, 'Peter',  154},
        { 3, 'Amy',  155},
        { 4, 'Hannah', 0},
        { 5, 'Michael', 0}
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
def add_coloums_in_many_products():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
    val = [
        { 154, 'Chocolate Heaven' },
        { 155, 'Tasty Lemons' },
        { 156, 'Vanilla Dreams' }
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
# เเสดงusers.nameกับproducts.nameโดยดูว่าusers.fav = products.idตัวไหนเหมือนกัน
def inner_join():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def left_join():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    LEFT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def right_join():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
if __name__ == "__main__":
    # try:
    #     create_table_users()
    # except:
    #     print('create_table_users is duplicate')
    # try:
    #     create_table_products()
    # except:
    #     print('create_table_products is duplicate')
    # try:
    #     add_coloums_in_many_users()
    # except:
    #     print('add_coloums_in_many_users is duplicate')
    # try:
    #     add_coloums_in_many_products()
    # except:
    #     print('add_coloums_in_many_products is duplicate')
    # ดูที่เหมือนกัน
    inner_join()
    print('---------------------------------------------')
    # ดูทั้งหมด
    left_join()
    print('---------------------------------------------')
    # ดูเเฉพาที่มี
    right_join()