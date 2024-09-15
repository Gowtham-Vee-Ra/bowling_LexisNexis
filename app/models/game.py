from datetime import datetime

games = {}  # In-memory store for games

class Game:
    """
    Class representing a bowling game.
    """
    def __init__(self, id, player_id=None):
        self.id = id
        self.player_id = player_id
        self.rolls = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
