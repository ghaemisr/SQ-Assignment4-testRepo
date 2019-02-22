import unittest
from gomoku.scoreboard import Scoreboard


class TestSetNewResult(unittest.TestCase):

    def setUp(self):
        self.sb = Scoreboard()

    def test_black_won(self):
        prev_score = self.sb.result['black']
        self.sb.set_new_result('black')
        self.assertEqual(prev_score + 1, self.sb.result['black'])
        # with mock.patch('gomoku.gameLogic.GameLogic') as MockGameLogic:
        #     MockGameLogic.return_value.find_winner.return_value = 'black'
        #     prev_score = self.sb.result['black']
        #     self.sb.set_new_result(MockGameLogic.return_value.find_winner())
        #     self.assertEqual(prev_score + 1, self.sb.result['black'])

    def test_white_won(self):
        prev_score = self.sb.result['white']
        self.sb.set_new_result('white')
        self.assertEqual(prev_score + 1, self.sb.result['white'])

    def test_tie_happened(self):
        prev_score = self.sb.result['tie']
        self.sb.set_new_result('tie')
        self.assertEqual(prev_score + 1, self.sb.result['tie'])

    def test_unexpected_input(self):
        with self.assertRaises(ValueError) as context:
            self.sb.set_new_result('Sara')
        self.assertTrue('Could not understand Sara as a winner' in str(context.exception))


class TestResetScoreboard(unittest.TestCase):

    def setUp(self):
        self.sb = Scoreboard()

    def test_black_won(self):
        expected_result = {'black': 0, 'white': 0, 'tie': 0}
        self.sb.reset_scoreboard()
        self.assertEqual(self.sb.result, expected_result)


if __name__ == '__main__':
    unittest.main()