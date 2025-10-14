from app.extensions import db
from app.models.associations import nurse_profile_departments

class Department(db.Model):
    # TODO: Department table:
    #  1. Akutpflege
    #  2. Langzeitpflege
    #  3. Psychiatrie
    #  4. Geriatrie
    #  5. Pädiatrie
    #  6. Intensivpflege
    #  7. Anästhesie
    #  8. Operationssaal
    #  9. Notfall
    #  10. Onkologie
    #  11. Rehabilitation
    #  12. Palliativpflege
    #  13. Spitex
    #  14. Wundpflege
    #  15. Dialyse
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    nurse_profiles = db.relationship('NurseProfile', secondary=nurse_profile_departments, back_populates='departments')