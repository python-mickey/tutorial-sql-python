import mysql.connector

def connect_db():
    # mysql://b1aca4230e5487:3f07fc3e@us-cdbr-iron-east-02.cleardb.net/heroku_f5e18a04c416e5e?reconnect=true
    # mysql://{Username}:{Password}@{Hostname}/{Database}?reconnect=true
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    #   host="us-cdbr-iron-east-02.cleardb.net",
    #   user="b1aca4230e5487",
    #   passwd="3f07fc3e",
    #   database="heroku_f5e18a04c416e5e"
    )
    return mydb
def create_db():
    mydb = connect_db()
    mycursor = mydb.cursor()
    # create database ซื่อ sql_python_tutorial
    mycursor.execute("CREATE DATABASE sql_python_tutorial")
# โชตารางทั้งหมด
def show_all_db():
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)
    
if __name__ == '__main__':
    try:
        create_db()
        print("create database success")
    except:
        print('you have name database duplicate')
    show_all_db()
