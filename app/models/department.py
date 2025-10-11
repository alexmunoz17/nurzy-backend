from app.extensions import db
from app.models.associations import user_departments

class Department(db.Model):
    # TODO: Department table:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    users = db.relationship('User', secondary=user_departments, back_populates='departments')