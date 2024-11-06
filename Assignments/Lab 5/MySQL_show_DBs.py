<<<<<<< HEAD
import mysql.connector
import GuiDBConfig as guiConf
# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
cursor = conn.cursor()
cursor.execute("SHOW DATABASES") 
print(cursor.fetchall())
=======
import mysql.connector
import GuiDBConfig as guiConf
# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)
cursor = conn.cursor()
cursor.execute("SHOW DATABASES") 
print(cursor.fetchall())
>>>>>>> a6dc84ab8684f0becaf28d314ed0711d4739a8d2
conn.close()