import unittest
from app import create_app
from app.models.game import games
from flask import json

class TestGameController(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.client = app.test_client()
        # Clear games before each test
        games.clear()

    def test_create_game(self):
        response = self.client.post('/games', json={})
        self.assertEqual(response.status_code, 201)
        self.assertIn('game_id', response.get_json())

    def test_create_game_with_invalid_player(self):
        response = self.client.post('/games', json={'player_id': 'nonexistent'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Player not found', response.get_data(as_text=True))

    def test_record_roll(self):
        # Create a game
        response = self.client.post('/games', json={})
        game_id = response.get_json()['game_id']
        # Record a valid roll
        response = self.client.post(f'/games/{game_id}/rolls', json={'pins': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['rolls'], [5])

    def test_record_roll_invalid_pins(self):
        # Create a game
        response = self.client.post('/games', json={})
        game_id = response.get_json()['game_id']
        # Record an invalid roll
        response = self.client.post(f'/games/{game_id}/rolls', json={'pins': -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid number of pins', response.get_data(as_text=True))

    def test_record_roll_invalid_game(self):
        response = self.client.post('/games/invalid_game_id/rolls', json={'pins': 5})
        self.assertEqual(response.status_code, 404)
        self.assertIn('Game not found', response.get_data(as_text=True))

    def test_get_score(self):
        # Create a game and record some rolls
        response = self.client.post('/games', json={})
        game_id = response.get_json()['game_id']
        self.client.post(f'/games/{game_id}/rolls', json={'pins': 10})
        self.client.post(f'/games/{game_id}/rolls', json={'pins': 3})
        self.client.post(f'/games/{game_id}/rolls', json={'pins': 6})
        # Get the score
        response = self.client.get(f'/games/{game_id}/score')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['score'], 28)

    def test_get_score_invalid_game(self):
        response = self.client.get('/games/invalid_game_id/score')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Game not found', response.get_data(as_text=True))

    def test_get_summary(self):
        # Create a game and record some rolls
        response = self.client.post('/games', json={})
        game_id = response.get_json()['game_id']
        self.client.post(f'/games/{game_id}/rolls', json={'pins': 10})
        # Get the summary
        response = self.client.get(f'/games/{game_id}/summary')
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.get_json())

    def test_get_summary_invalid_game(self):
        response = self.client.get('/games/invalid_game_id/summary')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Game not found', response.get_data(as_text=True))
