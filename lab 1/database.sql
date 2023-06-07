drop database hospital;

-- Create database
CREATE DATABASE hospital;

-- Use database
USE hospital;
CREATE TABLE roles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

-- Create users table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  login VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role_id INT NOT NULL,
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- Create illness table
CREATE TABLE illness(
  id INT AUTO_INCREMENT PRIMARY KEY,
  illness_name VARCHAR(50) NOT NULL,
  illness_type VARCHAR(50) NOT NULL,
  illness_description TEXT NOT NULL,
  price INT,
  status ENUM('pending', 'accepted', 'rejected', 'in-process', 'healed') NOT NULL DEFAULT 'pending',
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);


-- Create feedback table
CREATE TABLE feedbacks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  text TEXT,
  illness_id INT NOT NULL,
  master_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (illness_id) REFERENCES illness(id),
  FOREIGN KEY (master_id) REFERENCES users(id)
);

CREATE TABLE doctor_assignements(
  id INT AUTO_INCREMENT PRIMARY KEY,
  text TEXT,
  illness_id INT NOT NULL,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (illness_id) REFERENCES illness(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);