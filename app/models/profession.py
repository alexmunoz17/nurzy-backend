from app.extensions import db

class Profession(db.Model):
    # TODO: Profession table:
    #  1. Fachfrau / Fachmann Gesundheit (FaGe)
    #  2. Dipl. Pflegefachfrau / Pflegefachmann HF
    #  3. Pflegefachperson FH (Bachelor / Master)
    #  4. Assistentin / Assistent Gesundheit & Soziales (AGS)
    #  5. Pflegehelferin / Pflegehelfer SRK
    #  6. Fachfrau / Fachmann Betreuung (FaBe)
    #  7. Other
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    nurse_profiles = db.relationship('NurseProfile', back_populates='profession')
