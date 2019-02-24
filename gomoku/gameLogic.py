class GameLogic():

    def __init__(self):
        self.winner = "None"

    def check_horizontal(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        leftCount = 0
        rightCount = 0
        stone = chessboardMatrix[lastMoveRow][lastMoveCol]
        if stone == 0:
            return False
        for i in range(1, 5):
            if lastMoveCol - i >= 0:
                if chessboardMatrix[lastMoveRow][lastMoveCol - i] == stone:
                    leftCount = leftCount + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if lastMoveCol + i <= 18:
                if chessboardMatrix[lastMoveRow][lastMoveCol + i] == stone:
                    rightCount = rightCount + 1
                else:
                    break
            else:
                break
        if leftCount + rightCount + 1 >= 5:
            return True
        else:
            return False

    def check_vertical(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        upCount = 0
        downCount = 0
        stone = chessboardMatrix[lastMoveRow][lastMoveCol]
        if stone == 0:
            return False
        for i in range(1, 5):
            if lastMoveRow - i >= 0:
                if chessboardMatrix[lastMoveRow - i][lastMoveCol] == stone:
                    upCount = upCount + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if lastMoveRow + i <= 18:
                if chessboardMatrix[lastMoveRow + i][lastMoveCol] == stone:
                    downCount = downCount + 1
                else:
                    break
            else:
                break
        if upCount + downCount + 1 >= 5:
            return True
        else:
            return False

    def check_upper_diagonal(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        leftCount = 0
        rightCount = 0
        stone = chessboardMatrix[lastMoveRow][lastMoveCol]
        if stone == 0:
            return False
        for i in range(1, 5):
            if lastMoveRow - i >= 0 and lastMoveCol - i >= 0:
                if chessboardMatrix[lastMoveRow - i][lastMoveCol - i] == stone:
                    leftCount = leftCount + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if lastMoveRow + i <= 18 and lastMoveCol + i <= 18:
                if chessboardMatrix[lastMoveRow + i][lastMoveCol + i] == stone:
                    rightCount = rightCount + 1
                else:
                    break
            else:
                break
        if leftCount + rightCount + 1 >= 5:
            return True
        else:
            return False

    def check_lower_diagonal(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        leftCount = 0
        rightCount = 0
        stone = chessboardMatrix[lastMoveRow][lastMoveCol]
        if stone == 0:
            return False
        for i in range(1, 5):
            if lastMoveRow + i <= 18 and lastMoveCol - i >= 0:
                if chessboardMatrix[lastMoveRow + i][lastMoveCol - i] == stone:
                    leftCount = leftCount + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if lastMoveRow - i >= 0 and lastMoveCol + i <= 18:
                if chessboardMatrix[lastMoveRow - i][lastMoveCol + i] == stone:
                    rightCount = rightCount + 1
                else:
                    break
            else:
                break
        if leftCount + rightCount + 1 >= 5:
            return True
        else:
            return False

    def has_winner(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        if (self.check_horizontal(chessboardMatrix, lastMoveRow, lastMoveCol)
                or self.check_vertical(chessboardMatrix, lastMoveRow, lastMoveCol)
                or self.check_upper_diagonal(chessboardMatrix, lastMoveRow, lastMoveCol)
                or self.check_lower_diagonal(chessboardMatrix, lastMoveRow, lastMoveCol)):
            self.winner = "Black" if chessboardMatrix[lastMoveRow][lastMoveCol] == 1 else "White"
            return True
        else:
            return False
