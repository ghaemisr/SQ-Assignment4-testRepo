class Chessboard:
    class IllegalCoordinateException(Exception):
        def __init__(self, err="Illegal coordinate"):
            Exception.__init__(self, err)

    class IllegalPlayerException(Exception):
        def __init__(self, err="Illegal player"):
            Exception.__init__(self, err)

    class IllegalMoveException(Exception):
        def __init__(self, err="Occupied place"):
            Exception.__init__(self, err)

    def __init__(self):
        self.currentPlayer = "None"
        self.chessboardMatrix = []

    def init_chessboard(self):
        self.currentPlayer = "Black"
        self.chessboardMatrix = []
        for i in range(19):
            aCol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.chessboardMatrix.append(aCol)

    def get_current_player(self):
        self.currentPlayer = "White" if self.currentPlayer == "Black" else "Black"
        return self.currentPlayer

    def move(self, x, y, player):
        if type(x) != int or type(y) != int:
            raise self.IllegalCoordinateException
        if x < 0 or x > 18 or y < 0 or y > 18:
            raise self.IllegalCoordinateException
        if not (player == "White" or player == "Black"):
            raise self.IllegalPlayerException
        if self.chessboardMatrix[x][y] != 0:
            raise self.IllegalMoveException
        if player == "Black":
            self.chessboardMatrix[x][y] = 1
        elif player == "White":
            self.chessboardMatrix[x][y] = 2
