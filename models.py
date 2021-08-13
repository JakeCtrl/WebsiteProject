from database import db

class Note(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(100))
    date = db.Column("date", db.String(50))
    email = db.Column("email", db.String(100))
    def __init__(self, title, text, date, email):
        self.title = title
        self.text = text
        self.date = date
        self.email = email
