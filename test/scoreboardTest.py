import unittest
from unittest.mock import MagicMock
from gomoku.scoreboard import Scoreboard
from gomoku.chessboard import Chessboard


class TestWinner(unittest.TestCase):
    def test_score(self):
        fakeboard= Chessboard()
        fakeboard.get_winner = MagicMock(return_value="White")
        sb = Scoreboard()
        self.assertEqual(sb.score(fakeboard.get_winner()),"White")
        # self.assertEqual(scoreboard.score.assert_called_once_with('sara'), 'here is game scoreboard! sara')
        # scoreboard = Scoreboard()
        # scoreboard.score = MagicMock()
        # self.assertEqual(scoreboard.score.assert_called_once_with('sara'), 'here is game scoreboard! sara')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()