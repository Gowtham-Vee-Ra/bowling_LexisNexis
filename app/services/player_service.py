from uuid import uuid4
from app.models.player import Player, players
from app.models.game import games
from app.utils.game_logic import calculate_score

def create_player_service(name):
    if not name:
        raise ValueError("Name is required")
    player_id = str(uuid4())
    player = Player(id=player_id, name=name)
    players[player_id] = player
    return player_id

def get_player_statistics_service(player_id):
    if player_id not in players:
        raise KeyError("Player not found")
    player = players[player_id]
    total_games = len(player.games)
    total_score = 0
    highest_score = 0
    for game_id in player.games:
        game = games.get(game_id)
        if game:
            score = calculate_score(game.rolls)
            total_score += score
            if score > highest_score:
                highest_score = score
    average_score = total_score / total_games if total_games > 0 else 0
    stats = {
        'total_games': total_games,
        'average_score': average_score,
        'highest_score': highest_score
    }
    return stats
