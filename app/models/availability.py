from app.extensions import db

class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    # Flexibel, Frühdienst, Zwischendienst, Spätdienst, Geteilter Dienst, Nachtdienst