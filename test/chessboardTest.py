import unittest
from gomoku.chessboard import Chessboard

class TestChessboard(unittest.TestCase):
    def setUp(self):
        self.cb = Chessboard()

    def test_init_chessboard(self):
        self.cb.init_chessboard()
        self.assertEqual("Black", self.cb.currentPlayer)
        self.assertEqual(19, len(self.cb.chessboardMatrix))
        for i in range(19):
            self.assertEqual(19, len(self.cb.chessboardMatrix[i]))
            self.assertEqual(0, sum(self.cb.chessboardMatrix[i]))

    def test_get_current_player(self):
        self.cb.currentPlayer = "White"
        self.assertEqual("White", self.cb.get_current_player())
        self.assertEqual("Black", self.cb.get_current_player())

    def test_move(self):
        self.cb.init_chessboard()
        self.cb.move(0, 0, "Black")
        self.assertEqual(1, self.cb.chessboardMatrix[0][0])
        self.cb.move(18, 18, "White")
        self.assertEqual(2, self.cb.chessboardMatrix[18][18])
        self.assertRaises(self.cb.IllegalMoveException,self.cb.move,0,0,"White")
        self.assertRaises(self.cb.IllegalCoordinateException,self.cb.move,19,0,"White")
        self.assertRaises(self.cb.IllegalPlayerException,self.cb.move,10,10,"None")

if __name__ == '__main__':
    unittest.main()