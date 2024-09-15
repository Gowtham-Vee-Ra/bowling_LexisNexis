from flask import Blueprint, request, jsonify, abort
from app.services.player_service import (
    create_player_service,
    get_player_statistics_service,
)

player_bp = Blueprint('player_bp', __name__)

@player_bp.route('', methods=['POST'])
def create_player():
    """
    Create a new player.
    """
    data = request.get_json() or {}
    name = data.get('name')
    try:
        player_id = create_player_service(name)
        return jsonify({'player_id': player_id}), 201
    except ValueError as e:
        abort(400, description=str(e))

@player_bp.route('/<player_id>/statistics', methods=['GET'])
def get_player_statistics(player_id):
    """
    Get statistics for a specific player.
    """
    try:
        stats = get_player_statistics_service(player_id)
        return jsonify(stats), 200
    except KeyError as e:
        abort(404, description=str(e))
