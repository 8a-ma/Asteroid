import arcade
from collections import namedtuple
from managers.input_manager import InputManager


class Player(arcade.Sprite):
    def __init__(self, x: int, y: int, mass: int = 2, size=5):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(size, arcade.color.RED, outer_alpha=255)
        self.center_x = x
        self.center_y = y
        self.mass = mass

        self.max_speed = 5
        self.acceleration = 0.5
        self.static = False

        self.inputs = InputManager()

    def update(self, delta_time: float):
        if self.inputs.is_pressed(arcade.key.W):
            self.change_y += self.acceleration
        if self.inputs.is_pressed(arcade.key.S):
            self.change_y -= self.acceleration
        if self.inputs.is_pressed(arcade.key.A):
            self.change_x -= self.acceleration
        if self.inputs.is_pressed(arcade.key.D):
            self.change_x += self.acceleration

        self.change_x = arcade.math.clamp(self.change_x, -self.max_speed, self.max_speed)
        self.change_y = arcade.math.clamp(self.change_y, -self.max_speed, self.max_speed)

        super().update()
