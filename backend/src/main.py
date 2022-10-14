from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tournament.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)


from controller.tournament_controller import tournament_controller
app.register_blueprint(tournament_controller)


if __name__ == '__main__':
    app.run(debug=True)