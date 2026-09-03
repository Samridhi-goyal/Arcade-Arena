class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def start(self):
        raise NotImplementedError("Game must implement start()")

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
