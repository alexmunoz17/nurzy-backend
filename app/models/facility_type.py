from app.extensions import db

class FacilityType(db.Model):
    # TODO: Facility type table:
    #  1. Spital
    #  2. Pflegeheim
    #  3. Spitex
    #  4. Rehabilitationszentrum
    #  5. Psychiatrie
    #  6. Other
    __tablename__ = 'facility_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    facilities = db.relationship('Facility', back_populates='facility_type')
