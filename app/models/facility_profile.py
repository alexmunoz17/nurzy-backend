from datetime import datetime

from app.extensions import db

class FacilityProfile(db.Model):
    __tablename__ = 'facility_profile'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    users = db.relationship('User', back_populates='facility_profile')
    profile_complete = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    street = db.Column(db.String(80))
    city = db.Column(db.String(80))
    zip = db.Column(db.String(80))
    phone = db.Column(db.String(80))

    facility_id = db.Column(db.Integer, db.ForeignKey('facility.id'))
    facility = db.relationship('Facility', back_populates='facility_profiles')
