from app.extensions import db

class FacilityRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facility.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
