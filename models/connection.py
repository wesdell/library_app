import os
import mysql.connector as mysql
from dotenv import load_dotenv
load_dotenv()

mysqlUser = os.getenv('MYSQL_USER')
mysqlPassword = os.getenv('MYSQL_PASSWORD')
config = {
  'user': mysqlUser,
  'password': mysqlPassword,
  'host': '127.0.0.1',
  'database': 'your_database_name',
}

def connection():
  try:
    conn = mysql.connect(**config)
    print('Connected')
    return conn
  except mysql.Error as err:
    print(err)


