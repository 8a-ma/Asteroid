import arcade
from random import uniform, choice


class SpriteManager:
    def __init__(self, window):
        self.window = window
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
        self.asteroid_list.update()
        self.player_list.update()
        self.env_list.update()

        for asteroid in self.asteroid_list:
            speed = asteroid.change_x ** 2 + asteroid.change_y ** 2

            if speed > asteroid.max_speed ** 2:
                actual_speed = (speed**0.5)
                asteroid.change_x = (asteroid.change_x / actual_speed) * asteroid.max_speed
                asteroid.change_y = (asteroid.change_y / actual_speed) * asteroid.max_speed

        movable_entities = []
        movable_entities.extend(self.player_list)
        movable_entities.extend(self.asteroid_list)

        for sprite in movable_entities:
            self.check_bounds(sprite)

    def check_bounds(self, sprite):
        if getattr(sprite, 'static', False):
            return

        random_factor = uniform(0, 1)

        if sprite.left < 0 or sprite.right > self.window.width:
            sprite.change_x *= choice([-1, -2, -3]) * random_factor
            # Reposicionar para evitar que se quede "atrapado" en el borde
            if sprite.left < 0: sprite.left = 0
            if sprite.right > self.window.width: sprite.right = self.window.width

        # Rebote en Eje Y (Arriba o Abajo)
        if sprite.bottom < 0 or sprite.top > self.window.height:
            sprite.change_y *= choice([-1, -2, -3]) * random_factor
            # Reposicionar
            if sprite.bottom < 0: sprite.bottom = 0
            if sprite.top > self.window.height: sprite.top = self.window.height

    def draw(self):
        self.env_list.draw()
        self.asteroid_list.draw()
        self.player_list.draw()
