CREATE DATABASE IF NOT EXISTS Application;
USE Application;
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(255),
    email VARCHAR(256)
)
