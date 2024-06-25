-- Create the test database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update user 'hbnb_test' with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user on the specified test database and performance_schema
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Ensure all changes take effect immediately
FLUSH PRIVILEGES;

