from app.extensions import db

nurse_profile_departments = db.Table('nurse_profile_departments',
    db.Column('nurse_profile_id', db.Integer, db.ForeignKey('nurse_profile.id'), primary_key=True),
    db.Column('department_id', db.Integer, db.ForeignKey('department.id'), primary_key=True)
)