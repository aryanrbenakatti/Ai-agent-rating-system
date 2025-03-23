CREATE DATABASE IF NOT EXISTS real_estate;
USE real_estate;

-- Create 'agents' table
CREATE TABLE IF NOT EXISTS agents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sales INT NOT NULL,
    reviews FLOAT NOT NULL,
    response_time ENUM('Very Fast', 'Fast', 'Moderate', 'Slow') NOT NULL
);

-- Insert Sample Data
INSERT INTO agents (name, sales, reviews, response_time) VALUES
('John Doe', 50, 4.5, 'Fast'),
('Jane Smith', 70, 4.8, 'Very Fast'),
('Emily Johnson', 40, 4.2, 'Moderate'),
('Michael Brown', 55, 4.9, 'Fast'),
('Sarah Wilson', 60, 4.0, 'Fast'),
('David Miller', 30, 3.8, 'Slow');
