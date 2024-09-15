import unittest
from app import create_app
from app.models.player import players
from flask import json

class TestPlayerController(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.client = app.test_client()
        # Clear players before each test
        players.clear()

    def test_create_player(self):
        response = self.client.post('/players', json={'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('player_id', response.get_json())

    def test_create_player_no_name(self):
        response = self.client.post('/players', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name is required', response.get_data(as_text=True))

    def test_get_player_statistics(self):
        # Create a player
        response = self.client.post('/players', json={'name': 'Jane Doe'})
        player_id = response.get_json()['player_id']
        # Get statistics
        response = self.client.get(f'/players/{player_id}/statistics')
        self.assertEqual(response.status_code, 200)
        stats = response.get_json()
        self.assertEqual(stats['total_games'], 0)
        self.assertEqual(stats['average_score'], 0)
        self.assertEqual(stats['highest_score'], 0)

    def test_get_statistics_invalid_player(self):
        response = self.client.get('/players/invalid_player_id/statistics')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Player not found', response.get_data(as_text=True))
