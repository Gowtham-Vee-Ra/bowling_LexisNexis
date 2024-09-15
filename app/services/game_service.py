from uuid import uuid4
from datetime import datetime
from app.models.game import Game, games
from app.models.player import players
from app.utils.game_logic import (
    calculate_score,
    is_valid_roll,
)
from app.services.llm_service import generate_summary

def create_game_service(player_id=None):
    if player_id and player_id not in players:
        raise ValueError("Player not found")
    game_id = str(uuid4())
    game = Game(id=game_id, player_id=player_id)
    games[game_id] = game
    if player_id:
        players[player_id].games.append(game_id)
    return game_id

def record_roll_service(game_id, pins):
    if game_id not in games:
        raise KeyError("Game not found")
    if pins is None or not isinstance(pins, int) or not (0 <= pins <= 10):
        raise ValueError("Invalid number of pins")
    game = games[game_id]
    if not is_valid_roll(game.rolls, pins):
        raise ValueError("Invalid roll")
    game.rolls.append(pins)
    game.updated_at = datetime.utcnow()
    return game.rolls

def get_score_service(game_id):
    if game_id not in games:
        raise KeyError("Game not found")
    game = games[game_id]
    score = calculate_score(game.rolls)
    return score

def get_summary_service(game_id):
    if game_id not in games:
        raise KeyError("Game not found")
    game = games[game_id]
    score = calculate_score(game.rolls)
    summary = generate_summary(game.rolls, score)
    return summary
