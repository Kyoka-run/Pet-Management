-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS pet;

-- Select the database to use
USE pet;

-- Create a table to store the data uploaded by users
CREATE TABLE IF NOT EXISTS pet_data (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key, automatically incremented
    user_id INT NOT NULL,  -- Foreign key to identify the user who uploaded the data
    temperature DECIMAL(5,2) NOT NULL,  -- Temperature data, rounded to two decimal places
    heartbeat DECIMAL(5,2) NOT NULL,  -- Heartbeat data, rounded to two decimal places
    latitude DECIMAL(8,5) NOT NULL,  -- Latitude, rounded to five decimal places
    longitude DECIMAL(8,5) NOT NULL,  -- Longitude, rounded to five decimal places
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the data was uploaded
);
