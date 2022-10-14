from flask import Blueprint, request
from view.tournament_use_cases import create_tournament


tournament_controller = Blueprint("tournament_controller", __name__)

@tournament_controller.route("/tournament/new", methods=["POST"])
def process_create_tournament_request():
    request_data = request.json
    created_tournament = create_tournament(request_data)
    return created_tournament, 201
