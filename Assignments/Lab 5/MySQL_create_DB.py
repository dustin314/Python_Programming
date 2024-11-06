<<<<<<< HEAD
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE guidb")
except Error as e:
    print(f"Failed to create DB: 1007 (HY000): Can't create database 'guidb'; database exists")
finally:
    if conn.is_connected():
        cursor.close()
=======
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE guidb")
except Error as e:
    print(f"Failed to create DB: 1007 (HY000): Can't create database 'guidb'; database exists")
finally:
    if conn.is_connected():
        cursor.close()
>>>>>>> a6dc84ab8684f0becaf28d314ed0711d4739a8d2
        conn.close()