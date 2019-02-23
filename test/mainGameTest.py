import unittest
from unittest import mock
from gomoku.main import MainGame
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QSize


class TestOnResetClick(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = MainGame.MargaritaMixer()

    def test_reset_button(self):
        QTest.mouseClick(self.form.reset_button, Qt.LeftButton)
        with mock.patch('gomoku.gameLogic.GameLogic') as MockGameLogic:
            MockGameLogic.return_value.find_winner.return_value = 'black'
            prev_score = self.sb.result['black']
            self.sb.set_new_result(MockGameLogic.return_value.find_winner())
            self.assertEqual(prev_score + 1, self.sb.result['black'])


if __name__ == '__main__':
    unittest.main()