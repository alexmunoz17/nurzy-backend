from datetime import datetime

from app.extensions import db

class Subscription(db.Model):
    # TODO: Subscription table:
    #  1. Base
    #  2. Growth
    #  3. Elite
    #  4. Enterprise
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    facilities = db.relationship('Facility', back_populates='subscription')
