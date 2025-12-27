import arcade
import math

class Star(arcade.Sprite):
    def __init__(self, x: int, y: int, mass: int = 1.5, size: int = 40):
        super().__init__()

        self.texture = arcade.make_soft_circle_texture(size, arcade.color.GOLD, outer_alpha=255)

        self.center_x = x
        self.center_y = y
        self.mass = mass
