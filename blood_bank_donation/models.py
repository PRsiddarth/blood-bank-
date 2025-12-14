from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BloodType(db.Model):
    __tablename__ = 'blood_types'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), unique=True, nullable=False)
    donors = db.relationship('Donor', backref='blood_type', lazy=True)
    donations = db.relationship('Donation', backref='blood_type', lazy=True)
    inventory = db.relationship('BloodInventory', backref='blood_type', lazy=True)

class Donor(db.Model):
    __tablename__ = 'donors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('Male', 'Female', 'Other'), nullable=False)
    blood_type_id = db.Column(db.Integer, db.ForeignKey('blood_types.id'))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)
    last_donation_date = db.Column(db.Date)
    donations = db.relationship('Donation', backref='donor', lazy=True)

class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.id'))
    donation_date = db.Column(db.Date, nullable=False)
    quantity_ml = db.Column(db.Integer, nullable=False)
    blood_type_id = db.Column(db.Integer, db.ForeignKey('blood_types.id'))
    status = db.Column(db.Enum('Pending', 'Completed', 'Rejected'), default='Pending')
    notes = db.Column(db.Text)

class BloodInventory(db.Model):
    __tablename__ = 'blood_inventory'
    id = db.Column(db.Integer, primary_key=True)
    blood_type_id = db.Column(db.Integer, db.ForeignKey('blood_types.id'))
    quantity_ml = db.Column(db.Integer, default=0)
    expiry_date = db.Column(db.Date)
