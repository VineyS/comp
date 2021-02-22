import mysql.connector as mysql
import json

open_file = open('config.json', 'r')
auth = json.load(open_file)

host = auth['host']
user = auth['user']
password = auth['password']
#database = auth['database']

mysqldb  = mysql.connect(host = host, user = user, password = password)
cursor = mysqldb.cursor()
cursor.execute("CREATE DATABASE vineypsunu_librarymanagement")
cursor.execute("USE roxy_librarymanagement")
cursor.execute("CREATE TABLE AUTHENTICATION(id int(255) auto_increment, PRIMARY KEY(id), email varchar(256), password varchar(256), uuid text(256))")

print("MySQL Custom Credentials Setup Has Been Completed! Now Run index.py")
    

