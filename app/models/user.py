from datetime import datetime

from app.extensions import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    profile_pic = db.Column(db.Binary, nullable=False)
    profile_complete = db.Column(db.Boolean, nullable=False, default=False)

    # TODO: Role table: 1. Nurse, 2. Facility, (3. Partner - After launch)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    street = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    zip = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)

    # Nurse data
    cv = db.Column(db.Binary, unique=False, nullable=False)
    # TODO: Profession table
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'), nullable=False)
    experience = db.Column(db.Integer, unique=False, nullable=False)
    # TODO: Department table
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    # TODO: Availability table
    availability_id = db.Column(db.Integer, db.ForeignKey('availability.id'), nullable=False)

    caredit_count = db.Column(db.Integer, default=0, nullable=False)

    # TODO: Data protection regulation fields



    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
