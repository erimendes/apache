import mysql.connector
from mysql.connector import errorcode

db_config = {
    'host':'172.20.0.2',
    'user':'user',
    'password':'password',
    'database':'mydb',
    'charset':'utf8mb4',
    "collation":'utf8mb4_unicode_ci'
}

try:
    # cnx = mysql.connector.connect(user='root', 
    #                 password='senha_root', 
    #                 host='mariadb_container', 
    #                 database='seu_banco')
    cnx = mysql.connector.connect(
    **db_config
)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection successful!")
    cnx.close()
