-- MySQL script that prepares a MySQL server for an AirBnB clone application
-- if database hbnb_dev_db already exists , script should not fail
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- creates user hbnb_dev on server in localhost and sets password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- grant SELECT privilege on the database performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
