from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from models import db, Donor, Donation, BloodType, BloodInventory
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donors')
def donors():
    donors = Donor.query.all()
    return render_template('donors.html', donors=donors)

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        blood_type_id = int(request.form['blood_type'])
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')

        new_donor = Donor(name=name, age=age, gender=gender, blood_type_id=blood_type_id,
                         phone=phone, email=email, address=address)
        db.session.add(new_donor)
        db.session.commit()
        return redirect(url_for('donors'))
    blood_types = BloodType.query.all()
    return render_template('add_donor.html', blood_types=blood_types)

@app.route('/donations')
def donations():
    donations = Donation.query.all()
    return render_template('donations.html', donations=donations)

@app.route('/add_donation', methods=['GET', 'POST'])
def add_donation():
    if request.method == 'POST':
        donor_id = int(request.form['donor'])
        donation_date = datetime.strptime(request.form['donation_date'], '%Y-%m-%d').date()
        quantity_ml = int(request.form['quantity_ml'])
        blood_type_id = int(request.form['blood_type'])
        notes = request.form.get('notes')

        new_donation = Donation(donor_id=donor_id, donation_date=donation_date,
                               quantity_ml=quantity_ml, blood_type_id=blood_type_id, notes=notes)
        db.session.add(new_donation)

        # Update inventory
        inventory = BloodInventory.query.filter_by(blood_type_id=blood_type_id).first()
        if inventory:
            inventory.quantity_ml += quantity_ml
        else:
            inventory = BloodInventory(blood_type_id=blood_type_id, quantity_ml=quantity_ml)
            db.session.add(inventory)

        db.session.commit()
        return redirect(url_for('donations'))
    donors = Donor.query.all()
    blood_types = BloodType.query.all()
    return render_template('add_donation.html', donors=donors, blood_types=blood_types)

@app.route('/inventory')
def inventory():
    inventory = BloodInventory.query.all()
    return render_template('inventory.html', inventory=inventory)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add authentication logic here
        # For now, just redirect to index
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/api/donors', methods=['GET'])
def api_donors():
    donors = Donor.query.all()
    return jsonify([{
        'id': d.id,
        'name': d.name,
        'age': d.age,
        'gender': d.gender,
        'blood_type': d.blood_type.type if d.blood_type else None,
        'phone': d.phone,
        'email': d.email,
        'address': d.address,
        'last_donation_date': d.last_donation_date.isoformat() if d.last_donation_date else None
    } for d in donors])

@app.route('/api/donations', methods=['GET'])
def api_donations():
    donations = Donation.query.all()
    return jsonify([{
        'id': d.id,
        'donor_name': d.donor.name if d.donor else None,
        'donation_date': d.donation_date.isoformat(),
        'quantity_ml': d.quantity_ml,
        'blood_type': d.blood_type.type if d.blood_type else None,
        'status': d.status,
        'notes': d.notes
    } for d in donations])

@app.route('/api/inventory', methods=['GET'])
def api_inventory():
    inventory = BloodInventory.query.all()
    return jsonify([{
        'id': i.id,
        'blood_type': i.blood_type.type if i.blood_type else None,
        'quantity_ml': i.quantity_ml,
        'expiry_date': i.expiry_date.isoformat() if i.expiry_date else None
    } for i in inventory])

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            # Insert sample blood types if not exist
            if BloodType.query.count() == 0:
                blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
                for bt in blood_types:
                    db.session.add(BloodType(type=bt))
                db.session.commit()
        except Exception as e:
            print(f"Database error: {e}")
            print("Please ensure MySQL is running.")
    app.run(debug=True)
