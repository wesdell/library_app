from models.connection import *

def insertBooksFromDB(title, author, available):
  try:
    conn = connection()
    cursor = conn.cursor()
    query = 'INSERT INTO your_table_name (title, author, available) VALUES (%s, %s, %s)'
    data = (title, author, available)
    cursor.execute(query, data)
    conn.commit()
    conn.close()
    return 'Register inserted.'
  except mysql.Error as err:
    print(err)

def showBooksFromDB():
  data = []
  try:
    conn = connection()
    cursor = conn.cursor(buffered=True)
    query = 'SELECT id, title, author, available FROM your_table_name'
    cursor.execute(query)
    conn.commit()
    data = cursor.fetchall()
    conn.close()
  except mysql.Error as err:
    print(err.msg)
  return data

def searchBooksFromDB(id):
  data = []
  try:
    conn = connection()
    cursor = conn.cursor(buffered=True)
    query = 'SELECT id, title, author, available FROM your_table_name WHERE id = %s'
    cursor.execute(query, (id,))
    conn.commit()
    data = cursor.fetchall()
    conn.close()
  except mysql.Error as err:
    print(err)
  return data

def updateBooksFromDB(column, newValue, id):
  try:
    conn = connection()
    cursor = conn.cursor()
    if(column == '1'):
      query = 'UPDATE your_table_name SET title=%s WHERE id =%s'
    elif(column == '2'):
      query = 'UPDATE your_table_name SET author=%s WHERE id =%s'
    elif(column == '3'):
      query = 'UPDATE your_table_name SET available=%s WHERE id =%s'
    data = (newValue, id)
    cursor.execute(query, data)
    conn.commit()
    conn.close()
    return 'Register updated.'
  except mysql.Error as err:
    print(err)

def deleteBooksFromDB(id):
  try:
    conn = connection()
    cursor = conn.cursor()
    query = 'DELETE FROM your_table_name WHERE id = %s'
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return 'Register deleted.'
  except mysql.Error as err:
    print(err)