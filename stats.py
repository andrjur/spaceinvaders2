class Stats():
    """ статистика """

    def __init__(self):
        """  надо нАчать """
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        self.life = 2
        self.score = 0
