from app.extensions import db

class Availability(db.Model):
    # TODO: Availability table:
    #  1. Flexibel
    #  2. Frühdienst
    #  3. Zwischendienst
    #  4. Spätdienst
    #  5. Geteilter Dienst
    #  6. Nachtdienst
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    nurse_profiles = db.relationship('NurseProfile', back_populates='availability')
