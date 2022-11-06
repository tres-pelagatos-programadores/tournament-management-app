from flask import Flask
from controller.tournament_controller import tournament_controller
from model.tournament_models import db, Tournament, Player


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tournament.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
        db.create_all()

app.register_blueprint(tournament_controller)


if __name__ == '__main__':
    app.run(debug=True)
