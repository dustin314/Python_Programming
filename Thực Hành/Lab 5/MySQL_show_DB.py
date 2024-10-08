<<<<<<< HEAD
import mysql.connector
import GuiDBConfig as guiConf
# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
# create cursor
cursor = conn.cursor()
# execute command
cursor.execute("SHOW TABLES FROM guidb")
print(cursor.fetchall())
# close connection to MySQL
=======
import mysql.connector
import GuiDBConfig as guiConf
# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
# create cursor
cursor = conn.cursor()
# execute command
cursor.execute("SHOW TABLES FROM guidb")
print(cursor.fetchall())
# close connection to MySQL
>>>>>>> a6dc84ab8684f0becaf28d314ed0711d4739a8d2
conn.close()