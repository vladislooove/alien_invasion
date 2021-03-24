class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.is_game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.is_game_active = True