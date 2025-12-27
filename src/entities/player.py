import arcade
from collections import namedtuple


MoveState = namedtuple('MoveState', ['up', 'down', 'left', 'right'])

class Player(arcade.Sprite):
    def __init__(self, x, y, size=5):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(size, arcade.color.RED, outer_alpha=255)
        self.center_x = x
        self.center_y = y

        self.max_speed = 5
        self.acceleration = 0.5

        self.move = MoveState(up=False, down=False, left=False, right=False)


    def update(self, delta_time: float):
        if self.move.up:
            self.change_y += self.acceleration
        if self.move.down:
            self.change_y -= self.acceleration
        if self.move.left:
            self.change_x -= self.acceleration
        if self.move.right:
            self.change_x += self.acceleration

        self.change_x = arcade.math.clamp(self.change_x, -self.max_speed, self.max_speed)
        self.change_y = arcade.math.clamp(self.change_y, -self.max_speed, self.max_speed)

        super().update()
