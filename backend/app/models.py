from app import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    parsed_content = db.Column(db.JSON, nullable=False)

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    structure = db.Column(db.JSON, nullable=False)
