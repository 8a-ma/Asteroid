import arcade


class SpriteManager:
    def __init__(self):
        self.player_list = arcade.SpriteList()
        self.env_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

    def add_player(self, player):
        self.player_list.append(player)

    def add_environment(self, entity):
        self.env_list.append(entity)

    def add_astroid(self, asteroid):
        self.asteroid_list.append(asteroid)

    def update(self):
        for asteroid in self.asteroid_list:
            speed = asteroid.change_x ** 2 + asteroid.change_y ** 2

            if speed > asteroid.max_speed ** 2:
                actual_speed = (speed**0.5)
                asteroid.change_x = (asteroid.change_x / actual_speed) * asteroid.max_speed
                asteroid.change_y = (asteroid.change_y / actual_speed) * asteroid.max_speed

        self.asteroid_list.update()
        self.player_list.update()
        self.env_list.update()

    def draw(self):
        self.env_list.draw()
        self.asteroid_list.draw()
        self.player_list.draw()
