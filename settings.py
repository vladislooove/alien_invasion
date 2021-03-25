class Settings():
    def __init__(self):
        # Default params
        self.ship_speed_factor_default = 3
        self.bullet_speed_factor_default = 3
        self.alien_speed_factor_default = 1
        self.fleet_drop_speed_default = 5

        # Init game settings
        # Screen params
        self.screen_width = 1400
        self.screen_height = 830
        self.bg_color = (80, 38, 56)
        
        # Ship params
        self.ships_limit = 3
        self.ship_speed_factor = self.ship_speed_factor_default

        # Bullet params
        self.bullet_speed_factor = self.bullet_speed_factor_default
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien params
        self.alien_speed_factor = self.alien_speed_factor_default
        self.fleet_drop_speed = self.fleet_drop_speed_default

        # 1 == Right, -1 == Left
        self.fleet_direction = 1

    def reset_settings(self):
        self.ship_speed_factor = self.ship_speed_factor_default
        self.bullet_speed_factor = self.bullet_speed_factor_default
        self.alien_speed_factor = self.alien_speed_factor_default
        self.fleet_drop_speed = self.fleet_drop_speed_default
