import mysql.connector
def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    # ต้องcrate database ก่อนที่ไฟล์create_database.py 
    database="sql_python_tutorial"
#     host="us-cdbr-iron-east-02.cleardb.net",
#     user="b1aca4230e5487",
#     passwd="3f07fc3e",
#     # ต้องcrate database ก่อนที่ไฟล์create_database.py 
#     database="heroku_f5e18a04c416e5e"
    )
    return mydb
# --------------------show---------------------------
def show_table():
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
                print(x)
def show_coloumns_all():
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
def show_some_coloumns():
    #โชเเค่บางอย่างเช่นname กับaddress เท่านั้น 
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name, address FROM customers")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
def show_only_one_coloums():
        # โชเเค่ 1 rows
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchone()
        print(myresult)
# -----------------------------------------------
# -----------------------------------create_row--------------------------------------------------------------------
def create_table():
        mydb = connect_db()
        mycursor = mydb.cursor()
        # สร้าง table ซื่อ customers มีrows name เเละ address
        mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

def add_rows():
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("ALTER TABLE customers ADD COLUMN age INT(3)")
# ------------------------------------------------------------------------------------------------------------
# -----------------------------------create_coloums--------------------------------------------------------------------

def add_coloums_in_one():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # สร้างcoloums ซื่อ john กับ Highway 21 ซึ่งตรงกับ name กับ address ที่เราสร้างไปในcreate_table
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        #    ปริ้นเเถวสุดท้าย
        print("1 record inserted, ID:", mycursor.lastrowid)

def add_coloums_in_many():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # สร้างcoloums หลายๆcoloums ซึ่งตรงกับ name กับ address ที่เราสร้างไปในcreate_table
        val = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
        ]

        mycursor.executemany(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "was inserted.")
# ------------------------------------------------------------------------------------------------------------
# -------------------------------------------find-------------------------------------------------------------
# หาrow = address เเละ coloumns = Park Lane 38
def find_only_row_and_equal_coloums_something():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        # print(myresult[1][''])
        for x in myresult:
                print(x)
# หาrow = address เเละ coloumns = ที่ขึ้นต้นด้วยway
def find_only_row_and_equal_name_coloums_something():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM customers WHERE address Like '%way%'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)


# -------------------------------------sort-------------------------------------------------------------------
# ซื่อaไปz
def sort_coloums_name_aesc():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM customers ORDER BY name"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
# ซื่อzไปa
def sort_coloums_name_desc():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM customers ORDER BY name DESC"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
# ------------------------------------------------------------------------------------------------------------
# --------------------------------------delete----------------------------------------------------------------
# ลบทุกอย่างในrow address ที่เกี่ยวกับ Mountain 21
def delete_only_row_address_coloumns_something():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
# ------------------------------------------------------------------------------------------------------------
def delete_table():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "DROP TABLE customers"
        mycursor.execute(sql)
# ถ้าเป้นcustomer ให้ลบ เเต่ถ้าไม่ใช่จะไม่เกิดไรขึ้น
def delete_table_if_else():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "DROP TABLE IF EXISTS customers"
        mycursor.execute(sql)
def update_coloums():
        mydb = connect_db()
        mycursor = mydb.cursor()
        sql = "UPDATE customers SET address = %s WHERE address = %s"
        val = ("Canyon 123", "Valley 345")

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
def limit_coloums_one_to_five():
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers LIMIT 5")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)

def limit_coloums_three_to_seven():
        mydb = connect_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
if __name__ == "__main__":
        # --------------------show---------------------------
        # show_table()
        # show_coloumns_all()
        # show_some_coloumns()
        # show_only_one_coloums()
        # ---------------------------------------------------
        # --------------------create_table_and_rows---------------------------
        # try:
        #         create_table()
        #         print('create table success')
        # except:
        #         print('you have name table duplicate')
        # try:
        #         add_rows()
        #         print('create new coloum success')
        # except:
        #         print('you have name coloum duplicate')
        # ----------------------------------------------------
        # --------------------create_coloums---------------------------
        # add_coloums_in_one()
        # add_coloums_in_many()
        # ----------------------------------------------------
        # --------------------fine row----------------------------
        # find_only_row_and_equal_coloums_something()
        # find_only_row_and_equal_name_coloums_something()
        # ----------------------------------------------------
        # -------------------------------------sort-------------------------------------------------------------------
        # sort_coloums_name_aesc()
        # sort_coloums_name_desc()
        # ----------------------------------------------------
        # ----------------delete_coloums------------------------------
        # delete_only_row_address_coloumns_something()
        # ----------------------------------------------------
        # ----------------delete_rows------------------------------
        # try:
        #         delete_table()
        # except:
        #         print("not have a table")
        # delete_table_if_else()
        # ----------------------------------------------------
        # ---------------------update-------------------------
        # update_coloums()
        # ----------------------------------------------------
        # ---------------------limit-------------------------
        limit_coloums_one_to_five()
        limit_coloums_three_to_seven()
        # ----------------------------------------------------




