-- Blood Bank Donation Database Schema

CREATE DATABASE IF NOT EXISTS blood_bank;
USE blood_bank;

-- Blood Types Table
CREATE TABLE blood_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(10) NOT NULL UNIQUE
);

-- Donors Table
CREATE TABLE donors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    blood_type_id INT,
    phone VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    last_donation_date DATE,
    FOREIGN KEY (blood_type_id) REFERENCES blood_types(id)
);

-- Donations Table
CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT,
    donation_date DATE NOT NULL,
    quantity_ml INT NOT NULL,
    blood_type_id INT,
    status ENUM('Pending', 'Completed', 'Rejected') DEFAULT 'Pending',
    notes TEXT,
    FOREIGN KEY (donor_id) REFERENCES donors(id),
    FOREIGN KEY (blood_type_id) REFERENCES blood_types(id)
);

-- Blood Inventory Table
CREATE TABLE blood_inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    blood_type_id INT,
    quantity_ml INT DEFAULT 0,
    expiry_date DATE,
    FOREIGN KEY (blood_type_id) REFERENCES blood_types(id)
);

-- Insert sample blood types
INSERT INTO blood_types (type) VALUES ('A+'), ('A-'), ('B+'), ('B-'), ('AB+'), ('AB-'), ('O+'), ('O-');
