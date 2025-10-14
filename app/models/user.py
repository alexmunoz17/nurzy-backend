from datetime import datetime

from app.extensions import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', back_populates='users')
    nurse_profile_id = db.Column(db.Integer, db.ForeignKey('nurse_profile.id'))
    nurse_profile = db.relationship('NurseProfile', back_populates='users')
    facility_profile_id = db.Column(db.Integer, db.ForeignKey('facility_profile.id'))
    facility_profile = db.relationship('FacilityProfile', back_populates='users')
    profile_pic = db.Column(db.String(512))

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
