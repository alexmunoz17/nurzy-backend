from datetime import datetime

from app.extensions import db
from app.models.associations import nurse_profile_departments

class NurseProfile(db.Model):
    __tablename__ = 'nurse_profile'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    users = db.relationship('User', back_populates='nurse_profile')
    profile_complete = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    street = db.Column(db.String(80))
    city = db.Column(db.String(80))
    zip = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    cv = db.Column(db.String(512))
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'))
    profession = db.relationship('Profession', back_populates='nurse_profiles')
    experience_in_years = db.Column(db.Integer)
    departments = db.relationship('Department', secondary=nurse_profile_departments, back_populates='nurse_profiles')
    availability_id = db.Column(db.Integer, db.ForeignKey('availability.id'))
    availability = db.relationship('Availability', back_populates='nurse_profiles')
    caredit_count = db.Column(db.Integer, default=0)
