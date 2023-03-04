-- MySQL Database
CREATE DATABASE your_database_name

CREATE TABLE your_table_name(
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(100) NOT NULL,
  available VARCHAR(20) NOT NULL,
  CONSTRAINT pk_books_id PRIMARY KEY (id)
)
