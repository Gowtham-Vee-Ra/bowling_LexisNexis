import unittest
from app.utils.game_logic import calculate_score

class TestGameLogic(unittest.TestCase):
    def test_gutter_game(self):
        rolls = [0] * 20
        self.assertEqual(calculate_score(rolls), 0)

    def test_all_ones(self):
        rolls = [1] * 20
        self.assertEqual(calculate_score(rolls), 20)

    def test_one_spare(self):
        rolls = [5, 5, 3] + [0] * 17
        self.assertEqual(calculate_score(rolls), 16)

    def test_one_strike(self):
        rolls = [10, 3, 4] + [0] * 17
        self.assertEqual(calculate_score(rolls), 24)

    def test_perfect_game(self):
        rolls = [10] * 12
        self.assertEqual(calculate_score(rolls), 300)

    def test_tenth_frame_spare(self):
        rolls = [0] * 18 + [5, 5, 3]
        self.assertEqual(calculate_score(rolls), 13)

    def test_tenth_frame_strike(self):
        rolls = [0] * 18 + [10, 3, 4]
        self.assertEqual(calculate_score(rolls), 17)

    def test_invalid_rolls(self):
        rolls = [10] * 9 + [10, 10, 10, 10]
        score = calculate_score(rolls)
        self.assertEqual(score, 300)
