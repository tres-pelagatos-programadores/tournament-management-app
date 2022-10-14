from typing import Any
from model.tournament_models import db, Tournament, Player
from datetime import date


def create_tournament(request_data: dict[str, Any]) -> Tournament:
    name = request_data.get("name", None)
    players = request_data.get("players", [])
    start_date = request_data.get("start_date", date.today())

    player_objects = [Player(name=record.get("name", None), seed=record.get("seed", None)) for record in players]

    tournament = Tournament(
            name=name, 
            start_date=start_date,
            participants=player_objects
        )
    
    db.session.add(tournament)
    db.session.commit()

    return tournament


def find_tournament_by_id(tournament_id: int) -> Tournament:
    return Tournament.query.filter_by(id = tournament_id).first()
