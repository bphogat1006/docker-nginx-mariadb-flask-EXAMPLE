-- create db
-- it should be created automatically when mariadb creates the user specified in .env file
-- CREATE DATABASE flask_app_data;
USE flask_app_data;

-- create tables
CREATE TABLE `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
)
