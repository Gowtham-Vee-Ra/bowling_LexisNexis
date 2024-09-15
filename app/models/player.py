players = {}  # In-memory store for players

class Player:
    """
    Class representing a player.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.games = []
