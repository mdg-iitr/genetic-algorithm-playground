class Strategy:
    def __init__(self, encoding):
        self.encoding = encoding
        self.history = encoding[64:70]

    def move(self):
        index = int(''.join(str(x) for x in self.history), 2)
        return int(self.encoding[index])

    def update(self, last_game):
        self.history = self.history[2:] + last_game

    def reset_history(self):
        self.history = self.encoding[64:70]

    def __getitem__(self, item):
        return self.encoding[item]

    def __setitem__(self, key, value):
        self.encoding[key] = value
