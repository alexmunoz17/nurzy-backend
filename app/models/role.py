from app.extensions import db

class Role(db.Model):
    # TODO: Role table:
    #  1. Nurse
    #  2. Facility
    #  3. Partner - After launch
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    users = db.relationship('User', back_populates='role')
