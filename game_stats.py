class GameStats():
  def __init__(self, settings):
    self.settings = settings
    self.is_game_active = True
    self.reset_stats()

  def reset_stats(self):
    self.ships_left = self.settings.ships_limit
    self.is_game_active = True