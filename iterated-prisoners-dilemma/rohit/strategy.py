class Strategy:
    def __init__(self, encoding):
        self.encoding = encoding
        self.history = encoding[64:]

    def move(self):
        idx = int(self.history, 2)
        return int(self.encoding[idx])

    def update(self, moveA, moveB):
        self.history = self.history[2:] + str(moveA) + str(moveB)

    def reset(self):
        self.history = self.encoding[64:]

class TitForTat(Strategy):
    def __init__(self):
        self.history = 0

    def move(self):
        return self.history

    def update(self, lastGame):
        self.history = lastGame[1]

    def reset(self):
        self.history = 0

alwaysCoOp = Strategy("0" * 70)
alwaysDef  = Strategy("1" * 70)
