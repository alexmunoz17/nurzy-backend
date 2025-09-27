from datetime import datetime

from app.extensions import db

class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    # TODO: Subscription table: 1. Base, 2. Growth, 3. Elite, 4. Enterprise (No plan for nurse)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)

    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    logo = db.Column(db.Binary(128), nullable=False)

    street = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    zip = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    # TODO: Facility type table
    type_id = db.Column(db.Integer, db.ForeignKey('facility_type.id'), nullable=False)
