-- mariadb runs this script ONLY the FIRST time the mariadb image is created.
-- subsequent builds do NOT run this again.
-- keep it updated with the latest schema for all databases.
-- to run this script again, the db-data volume must be deleted.

-- create database(s)
CREATE DATABASE flask_app_data;

-- create main user with all privileges on all existing databases
-- *** must remember to grant priviliges to main user to any new databases created after initial mariadb image is created
GRANT ALL PRIVILEGES ON *.* TO 'main'@'%';
FLUSH PRIVILEGES;

-- create tables
USE flask_app_data;
CREATE TABLE `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
)
