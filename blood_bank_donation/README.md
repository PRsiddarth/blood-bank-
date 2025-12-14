# Blood Bank Donation System

A full-stack web application for managing blood bank donations, built with Flask (Python) for the backend and HTML/CSS/JavaScript with Bootstrap for the frontend. Uses MySQL for data storage.

## Features

- Donor registration and management
- Donation tracking
- Blood inventory management
- Responsive web interface
- RESTful API endpoints

## Prerequisites

- Python 3.7+
- MySQL Server
- XAMPP (for easy MySQL setup on Windows)

## Installation

1. Clone or download the project files.

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up MySQL database:
   - Start XAMPP and ensure MySQL is running.
   - Create a database named `blood_bank`.
   - Run the SQL script in `database.sql` to create tables and insert initial data.

4. Update database configuration in `config.py` if needed (default: root user, no password).

## Running the Application

1. Navigate to the project directory:
   ```
   cd blood_bank_donation
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your browser and go to `http://localhost:5000`

## Project Structure

```

```

## API Endpoints

- `GET /api/donors` - Get all donors
- `GET /api/donations` - Get all donations
- `GET /api/inventory` - Get blood inventory

## Technologies Used

- **Backend:** Flask, SQLAlchemy, MySQL
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** MySQL
- **Version Control:** Git

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
blood_bank_donation/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── config.py              # Configuration settings
├── database.sql           # Database schema
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── donors.html
│   ├── add_donor.html
│   ├── donations.html
│   ├── add_donation.html
│   └── inventory.html
├── static/                # Static files
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── README.md