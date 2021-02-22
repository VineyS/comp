#######################################
######     IMPORTING MODULES     ######
#######################################
import json
import mysql.connector as mysql
from mysql.connector.errors import Error

#######################################
######    MYSQLAUTHENTICATION    ######
#######################################
open_file = open('config.json', 'r')
auth = json.load(open_file)

host = auth['host']
user = auth['user']
password = auth['password']
database = auth['database']
def db():
    try:
        mydb_auth = mysql.connect(host = host, user = user, password = password, database = database)
    except Error as e:
        print("Connection Refused!!")
        print(e)
    else:
        db_auth = mydb_auth
        return db_auth

def db_login():
    try: 
        sql_login_auth = mysql.connect(host = host, user = user, password = password, database = database)
    except Error as e:
        print("Connection Refused!")
        print(e)
    else:
        login_auth = sql_login_auth
        return login_auth

    


