import os
from tabulate import tabulate
from models.book import *

def start():
  os.system('cls')
  while (True):
    print('Select one option:')
    print('\t1. Add book')
    print('\t2. Show all books')
    print('\t3. Search book')
    print('\t4. Update book')
    print('\t5. Delete book')
    print('\t6. Exit')
    option = input('Choose an option: ')
    if option == '1':
      insert_books()
    elif option == '2':
      show_books()
    elif option == '3':
      search_books()
    elif option == '4':
      update_books()
    elif option == '5':
      delete_books()
    elif option == '6':
      break

def table_grid(data):
  os.system('cls')
  headers = ['ID', 'TITLE', 'AUTHOR', 'AVAILABLE']
  table = tabulate(data, headers, tablefmt='fancy_grid')
  print(table)

def insert_books():
  title = input('Insert book title: ')
  author = input('Insert book author: ')
  available = input('Is available this book? Available/Not Available: ')
  response = insertBooksFromDB(title, author, available)
  os.system('cls')
  print(response)

def show_books():
  response = showBooksFromDB() 
  table_grid(response)

def search_books():
  bookId = input('Insert book id to search: ')
  response = searchBooksFromDB(bookId)
  table_grid(response)

def update_books():
  show_books()
  bookId = input('Insert book id to update: ')
  print('Select the field number that you want to update:\n1. Title\n2. Author\n3. Available')
  column = input('Field number: ')
  value = input('Insert the new value: ')
  response = updateBooksFromDB(column, value, bookId)
  os.system('cls')
  print(response)

def delete_books():
  show_books()
  bookId = input('Insert book id to delete: ')
  response = deleteBooksFromDB(bookId)
  os.system('cls')
  print(response)

start()