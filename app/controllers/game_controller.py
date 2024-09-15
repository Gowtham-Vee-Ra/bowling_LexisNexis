# game_controller.py

import openai
from flask import Blueprint, request, jsonify, abort
from app.services.game_service import (
    create_game_service,
    record_roll_service,
    get_score_service,
    get_summary_service,
)

game_bp = Blueprint('game_bp', __name__)

@game_bp.route('', methods=['POST'])
def create_game():
    """
    Create a new game.
    """
    data = request.get_json() or {}
    player_id = data.get('player_id')
    try:
        game_id = create_game_service(player_id)
        return jsonify({'game_id': game_id}), 201
    except ValueError as e:
        abort(400, description=str(e))

@game_bp.route('/<game_id>/rolls', methods=['POST'])
def record_roll(game_id):
    """
    Record a roll for a specific game.
    """
    data = request.get_json() or {}
    pins = data.get('pins')
    try:
        rolls = record_roll_service(game_id, pins)
        return jsonify({'rolls': rolls}), 200
    except KeyError as e:
        abort(404, description=str(e))
    except ValueError as e:
        abort(400, description=str(e))

@game_bp.route('/<game_id>/score', methods=['GET'])
def get_score(game_id):
    """
    Get the current score of the game.
    """
    try:
        score = get_score_service(game_id)
        return jsonify({'score': score}), 200
    except KeyError as e:
        abort(404, description=str(e))

@game_bp.route('/<game_id>/summary', methods=['GET'])
def get_summary(game_id):
    """
    Get a natural language summary of the current game state.
    """
    try:
        summary = get_summary_service(game_id)
        return jsonify({'summary': summary}), 200
    except KeyError as e:
        abort(404, description=str(e))
    except Exception as e:
        abort(500, description=str(e))
