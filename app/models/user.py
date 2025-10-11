from datetime import datetime

from app.extensions import db, bcrypt
from app.models.associations import user_departments

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', back_populates='users')
    profile_pic = db.Column(db.String(512))
    profile_complete = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    street = db.Column(db.String(80))
    city = db.Column(db.String(80))
    zip = db.Column(db.String(80))
    phone = db.Column(db.String(80))

    # Nurse data
    cv = db.Column(db.String(512))
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'))
    profession = db.relationship('Profession', back_populates='users')
    experience_in_years = db.Column(db.Integer)
    departments = db.relationship('Department', secondary=user_departments, back_populates='users')
    # TODO: Availability table
    availability_id = db.Column(db.Integer, db.ForeignKey('availability.id'))
    caredit_count = db.Column(db.Integer, default=0)

    # TODO: Data protection regulation fields



    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
