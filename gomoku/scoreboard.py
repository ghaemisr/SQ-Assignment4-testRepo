class Scoreboard:

    def __init__(self):
        self.result = {'black': 0, 'white': 0, 'tie': 0}

    def set_new_result(self, winner):
        """
        :param winner: the winner is an input
        :return: There is no return for this function
        """
        if winner == 'black':
            self.result['black'] += 1
        elif winner == 'white':
            self.result['white'] += 1
        elif winner == 'tie':
            self.result['tie'] += 1
        else:
            raise ValueError('Could not understand ' + winner + ' as a winner')

    def reset_scoreboard(self):
        """
        :return: there is no return
        """
        self.result = {'black': 0, 'white': 0, 'tie': 0}
