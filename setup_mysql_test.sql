-- create database, which is named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user who is named hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to user on the just created database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privilege to user on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
