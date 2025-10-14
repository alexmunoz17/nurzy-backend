from datetime import datetime

from app.extensions import db

class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    facility_profiles = db.relationship('FacilityProfile', back_populates='facility')
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    subscription = db.relationship('Subscription', back_populates='facilities')
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))
    logo = db.Column(db.String(512))
    street = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    zip = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    website = db.Column(db.String(80))
    number_of_employees = db.Column(db.Integer)
    facility_type_id = db.Column(db.Integer, db.ForeignKey('facility_type.id'), nullable=False)
    facility_type = db.relationship('FacilityType', back_populates='facilities')
    number_of_seats = db.Column(db.Integer)
