# CRUD APPLICATION

## About the project:

A simple CRUD app in the console, where you can store your library stock.

## How to use:

### 1. Step

First clone the project with the next command: (Do not copy the _%_ symbol)

```
$ git clone https://github.com/wesdell/library_app.git
```

Then, run the following commands:

```
$ pip install python-dotenv
```

```
$ pip install tabulate
```

```
$ pip install mysql-connector-python
```

### 2. Step

Next, change the file name from .example.env to .env.

From:

```
|---models/
|---.example.env
|---.gitignore
└---main.py
```

To:

```
|---models/
|---.env
|---.gitignore
└---main.py
```

Then, put your data in the defined variables on the env file.

### 3. Step

Go to your MySQL panel and create your own database and table. You have the table structure in the schema.sql file.

```
|___models/
|    └---schema.sql
|---.env
|---.gitignore
└---main.py
```

### 4. Step

Make the following changes in these files.

```
|___models/
|    |---book.py
|    └---connection.py
|---.env
|---.gitignore
└---main.py
```

- In the connection.py file open the config object and put your database name in the database property.
- In the book.py file put your table name in each SQL statement into the functions.

## Common functionalities:

- The user can save and view their books
- The user can update and delete their books

## Build with:

- Python
- MySQL

## Key concepts:

- CRUD
- SQL
- Console app
