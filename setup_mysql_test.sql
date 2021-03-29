-- MySQL script that prepares a MySQL server for an AirBnB clone application
-- if database hbnb_test_db already exists , script should not fail
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- creates user hbnb_test on server in localhost and sets password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grant SELECT privilege on the database performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
