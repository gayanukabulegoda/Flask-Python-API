CREATE DATABASE python_intro;

USE python_intro;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);