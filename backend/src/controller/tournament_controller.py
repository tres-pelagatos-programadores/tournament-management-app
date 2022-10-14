from typing import Dict, Any
from flask import Blueprint, request
from view.tournament_use_cases import create_tournament, find_tournament_by_id


tournament_controller = Blueprint("tournament_controller", __name__)


@tournament_controller.route("/tournament/new", methods=["POST"])
def process_create_tournament_request():
    request_data = request.json
    created_tournament = create_tournament(request_data)
    return created_tournament.to_dict(), 201


@tournament_controller.route("/tournament/<id>", methods=["GET"])
def get_tournament_by_id(id: int) -> Dict[str, Any]:
    found_tournament = find_tournament_by_id(tournament_id=id)
    return found_tournament.to_dict(), 200
