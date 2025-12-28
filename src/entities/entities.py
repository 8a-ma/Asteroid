import math
import arcade
import random


class Star(arcade.Sprite):
    def __init__(self, x: int, y: int, mass: int = 1.5, size: int = 40):
        super().__init__()

        self.texture = arcade.make_soft_circle_texture(size, arcade.color.GOLD, outer_alpha=255)

        self.center_x = x
        self.center_y = y
        self.mass = mass
        self.static = True

class Asteroid(arcade.Sprite):
    def __init__(self, x: int, y: int, mass: int = 1, size: int = 25):
        super().__init__()

        self.texture = arcade.make_soft_circle_texture(size, arcade.color.ARTICHOKE, outer_alpha=255)

        self.center_x = x
        self.center_y = y
        self.mass = mass

        self.max_speed = 10
        self.static = False

    def init_velocity_towards(self, target_x, target_y):
        diff_x = target_x - self.center_x
        diff_y = target_y - self.center_y
        dist = math.sqrt(diff_x ** 2 + diff_y ** 2)

        speed = random.uniform(2, 5)
        self.change_x = (diff_x / dist) * speed
        self.change_y = (diff_y / dist) * speed


    def update(self, delta_time: float):
        super().update()
