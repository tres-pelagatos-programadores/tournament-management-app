from main import db




class Tournament(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    participants = db.relationship('Player', backref='tournament', lazy=True)


class Player(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(50))
    seed = db.Column(db.Integer)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
