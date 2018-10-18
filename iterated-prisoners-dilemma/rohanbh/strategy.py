

class Strategy:
    """A strategy remembers the previous 3 games and makes the next move based on the 
    game history. A cooperation (C) is represented by 0 while a defection (D) is 
    represented by 1"""

    def __init__(self, encoding):
        self.encoding = encoding
        # init history with initial assumptions
        self.history = self.encoding[64:70]

    def move(self):
        index = int(''.join(str(x) for x in self.history), 2)
        return self.encoding[index]

    def update(self, last_game):
        self.history = self.history[2:] + last_game



