from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller.tournament_controller import tournament_controller


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

app.register_blueprint(tournament_controller)


if __name__ == '__main__':
    app.run(debug=True)