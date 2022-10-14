from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Tournament(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    participants = db.relationship('Player', backref='tournament', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date,
            "participants": [player.to_dict() for player in self.participants]
        }


class Player(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(50))
    seed = db.Column(db.Integer)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "seed": self.seed
        }
