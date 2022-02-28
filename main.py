import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='newbase',
)

mycursor = mydb.cursor()
print("Enter you login: ")
log = input()
print("Enter you password: ")
pas = input()
mycursor.execute(" SELECT*FROM user WHERE name =%s AND password =%s", (log, pas))
myresult = mycursor.fetchall()
if myresult:
    print("successfully")
else:
    print("enter correct login and password")
